# File: infra/pyinfra/verify_vm.pyinfra.py

import os
import requests
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from pathlib import Path
import sys

# Disable SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

class ProxmoxVMVerifier:
    def __init__(self):
        # Load .env from current script directory (sibling file)
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
        response = requests.get(url, headers=self.headers, verify=False)
        print(f"📡 GET {url} → {response.status_code}")
        response.raise_for_status()
        return response.json()

    def verify_vm(self, vmid):
        nodes = self.get("/nodes")['data']
        for node in nodes:
            vm_list = self.get(f"/nodes/{node['node']}/qemu")['data']
            for vm in vm_list:
                if str(vm['vmid']) == str(vmid):
                    print(f"✅ Found VM {vm['name']} (VMID: {vmid}) on node {node['node']} with status: {vm['status']}")
                    return
        print(f"❌ VM with ID {vmid} not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_vm.pyinfra.py <vmid>")
        sys.exit(1)

    vmid = sys.argv[1]
    verifier = ProxmoxVMVerifier()
    verifier.verify_vm(vmid)
