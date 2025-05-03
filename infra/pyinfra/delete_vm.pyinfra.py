# File: infra/pyinfra/delete_vm.pyinfra.py

import os
import requests
import json
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

# Load .env variables
load_dotenv()

API_BASE = os.getenv("PROXMOX_API")
USER = os.getenv("PROXMOX_USER")
TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")
TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")

if not API_BASE or not USER or not TOKEN_ID or not TOKEN_SECRET:
    raise ValueError("❌ Required Proxmox credentials are missing.")

HEADERS = {
    "Authorization": f"PVEAPIToken={USER}!{TOKEN_ID}={TOKEN_SECRET}"
}

def delete_vm(node, vmid):
    confirm = input(f"⚠️  Are you sure you want to delete VMID {vmid} on node {node}? Type YES to confirm: ")
    if confirm != "YES":
        print("❌ Aborted by user.")
        return

    print(f"🔧 Sending delete request for VMID {vmid} on node {node}...")
    url = f"{API_BASE}/nodes/{node}/qemu/{vmid}"
    response = requests.delete(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    print(f"🗑️ Successfully deleted VMID {vmid} on node {node}.")

if __name__ == "__main__":
    try:
        node = input("Node name (e.g., pve-tde): ").strip()
        vmid = input("VMID to delete: ").strip()
        if not vmid.isdigit():
            raise ValueError("VMID must be numeric.")
        delete_vm(node, int(vmid))
    except Exception as e:
        print(f"❌ Error: {e}")
