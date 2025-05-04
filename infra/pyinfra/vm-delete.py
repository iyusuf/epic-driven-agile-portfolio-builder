# File: infra/pyinfra/vm-delete.pyinfra.py

import os
import requests
import sys
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from pathlib import Path

# Disable SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

class ProxmoxVMDeleter:
    def __init__(self):
        env_path = Path(__file__).resolve().parent / ".env"
        load_dotenv(dotenv_path=env_path)

        host = os.getenv("PROXMOX_HOST")
        self.api_base = f"https://{host}:8006/api2/json" if host else None
        self.user = os.getenv("PROXMOX_USER")
        self.token_id = os.getenv("PROXMOX_TOKEN_NAME")
        self.token_secret = os.getenv("PROXMOX_TOKEN_SECRET")

        if not all([self.api_base, self.user, self.token_id, self.token_secret]):
            raise ValueError("❌ Missing one or more required environment variables.")

        self.headers = {
            "Authorization": f"PVEAPIToken={self.user}!{self.token_id}={self.token_secret}"
        }

    def get(self, endpoint):
        url = f"{self.api_base}{endpoint}"
        response = requests.get(url, headers=self.headers, verify=False, timeout=5)
        response.raise_for_status()
        return response.json()

    def delete_vm(self, vmid):
        nodes = self.get("/nodes")['data']
        for node in nodes:
            vms = self.get(f"/nodes/{node['node']}/qemu")['data']
            for vm in vms:
                if str(vm['vmid']) == str(vmid):
                    confirm = input(f"⚠️ Are you sure you want to delete VM {vm['name']} (VMID: {vmid}) on {node['node']}? Type YES to confirm: ")
                    if confirm != "YES":
                        print("❌ Deletion aborted.")
                        return
                    if vm.get("status") == "running":
                        print("❌ Cannot delete VM while it is running. Please shut it down first.")
                        return
                    del_url = f"/nodes/{node['node']}/qemu/{vmid}"
                    del_response = requests.delete(f"{self.api_base}{del_url}", headers=self.headers, verify=False, timeout=5)
                    del_response.raise_for_status()
                    print(f"🗑️ VM {vmid} deleted successfully from node {node['node']}")
                    return
        print(f"❌ VM with ID {vmid} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vm-delete.pyinfra.py <vmid>")
        sys.exit(1)

    vmid = sys.argv[1]
    deleter = ProxmoxVMDeleter()
    deleter.delete_vm(vmid)
