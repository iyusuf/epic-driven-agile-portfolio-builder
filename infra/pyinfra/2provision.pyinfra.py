# File: infra/pyinfra/provision.pyinfra.py

import os
import json
import requests
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

# Load environment variables
load_dotenv()

API_BASE = os.getenv("PROXMOX_API")
USER = os.getenv("PROXMOX_USER")
TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")
TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")

if not API_BASE or not USER or not TOKEN_ID or not TOKEN_SECRET:
    raise ValueError("Missing Proxmox credentials in environment.")

HEADERS = {
    "Authorization": f"PVEAPIToken={USER}!{TOKEN_ID}={TOKEN_SECRET}"
}

# Load discovered settings from explore output
with open("infra/pyinfra/explore.proxmox.json") as f:
    data = json.load(f)

node = data["node"]
template_vmid = data["template"]["vmid"]
template_name = data["template"]["name"]
target_storage = data["storage"]
target_bridge = data["bridge"]

# Customize new VM settings
new_vmid = 9521
new_vm_name = "dev-sandbox-1"

# Clone VM
print(f"🚀 Cloning VM from template {template_name} (VMID: {template_vmid})...")
clone_endpoint = f"{API_BASE}/nodes/{node}/qemu/{template_vmid}/clone"
clone_data = {
    "newid": new_vmid,
    "name": new_vm_name,
    "target": node,
    "full": 1,           # full clone
    "storage": target_storage
}

response = requests.post(clone_endpoint, headers=HEADERS, data=clone_data, verify=False)
if response.status_code == 200:
    print(f"✅ VM clone triggered for '{new_vm_name}' (VMID: {new_vmid})")
else:
    print(f"❌ Clone failed: {response.status_code}")
    print(response.text)