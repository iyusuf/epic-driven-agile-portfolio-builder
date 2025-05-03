# File: infra/pyinfra/provision.pyinfra.py

import os
import requests
import json
import random
import string
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress SSL warnings for self-signed certs
urllib3.disable_warnings(InsecureRequestWarning)

# Load .env file
load_dotenv()

# Load Proxmox API details from environment
API_BASE = os.getenv("PROXMOX_API")
USER = os.getenv("PROXMOX_USER")
TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")
TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")

if not API_BASE or not USER or not TOKEN_ID or not TOKEN_SECRET:
    raise ValueError("❌ Environment variables PROXMOX_API, PROXMOX_USER, PROXMOX_TOKEN_ID, and PROXMOX_TOKEN_SECRET must be set.")

HEADERS = {
    "Authorization": f"PVEAPIToken={USER}!{TOKEN_ID}={TOKEN_SECRET}"
}

def post(endpoint, data):
    url = f"{API_BASE}{endpoint}"
    response = requests.post(url, headers=HEADERS, data=data, verify=False)
    if not response.ok:
        print("❌ Response content:", response.text)
    response.raise_for_status()
    return response.json() if response.text else {}

# Load discovery data using dynamic path
explore_path = os.path.join(os.path.dirname(__file__), "explore.proxmox.json")
os.makedirs(os.path.dirname(explore_path), exist_ok=True)

with open(explore_path) as f:
    discovery = json.load(f)

node = discovery["node"]
template_vmid = discovery["template"]["vmid"]
storage = discovery["storage"]
bridge = discovery["bridge"]

# Select valid VM image storage
valid_storages = ["local-lvm", "local-lvm2"]
selected_storage = storage if storage in valid_storages else "local-lvm"

# Generate new VM ID and name
new_vmid = random.randint(2000, 2999)
random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
new_name = f"dev-vm-{random_suffix}"

print(f"🚀 Cloning template VMID {template_vmid} as {new_name} (VMID: {new_vmid}) with full clone to storage '{selected_storage}'...")

# Perform full clone
clone_data = {
    "newid": new_vmid,
    "name": new_name,
    "full": 1,
    "storage": selected_storage
}
post(f"/nodes/{node}/qemu/{template_vmid}/clone", clone_data)
print("✅ Full clone initiated.")
