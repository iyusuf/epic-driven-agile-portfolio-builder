# File: infra/pyinfra/postprovision.pyinfra.py

import os
import json
import requests
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

# Load .env file
load_dotenv()

API_BASE = os.getenv("PROXMOX_API")
USER = os.getenv("PROXMOX_USER")
TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")
TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")

if not API_BASE or not USER or not TOKEN_ID or not TOKEN_SECRET:
    raise ValueError("❌ Missing required environment variables.")

HEADERS = {
    "Authorization": f"PVEAPIToken={USER}!{TOKEN_ID}={TOKEN_SECRET}"
}

def fetch(endpoint):
    url = f"{API_BASE}{endpoint}"
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    return response.json()["data"]

# Load previous discovery info
explore_path = os.path.join(os.path.dirname(__file__), "explore.proxmox.json")
with open(explore_path) as f:
    context = json.load(f)

node = context["node"]

print(f"🔍 Checking provisioned VMs on node '{node}'...")

vms = fetch(f"/nodes/{node}/qemu")
provisioned = [
    {
        "name": vm["name"],
        "vmid": vm["vmid"],
        "status": vm.get("status", "unknown")
    }
    for vm in vms
    if vm.get("template") != 1 and vm["name"].startswith("dev-vm-")
]

print(f"✅ Found {len(provisioned)} provisioned VMs:")
for vm in provisioned:
    print(f"  - {vm['name']} (VMID: {vm['vmid']}, Status: {vm['status']})")

# Save provisioned VM list
summary_path = os.path.join(os.path.dirname(__file__), "provisioned-vms.json")
with open(summary_path, "w") as out:
    json.dump(provisioned, out, indent=2)

print("\n🧾 Summary saved to provisioned-vms.json")
