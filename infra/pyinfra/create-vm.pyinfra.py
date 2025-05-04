# File: infra/pyinfra/create_vm.pyinfra.py

import os
import json
import requests
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

# Load .env
load_dotenv()

API_BASE = os.getenv("PROXMOX_API")
USER = os.getenv("PROXMOX_USER")
TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")
TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")

HEADERS = {
    "Authorization": f"PVEAPIToken={USER}!{TOKEN_ID}={TOKEN_SECRET}"
}

def post(endpoint, payload):
    url = f"{API_BASE}{endpoint}"
    response = requests.post(url, headers=HEADERS, json=payload, verify=False)
    print(f"🔁 POST {url} → {response.status_code}")
    if response.content:
        print(response.text)
    response.raise_for_status()
    return response.json()

# Load input JSON
with open("vm-create.json") as f:
    vm = json.load(f)

print(f"🚀 Cloning VM from template {vm['template_vmid']} → {vm['vmid']} ({vm['name']})")

clone_data = {
    "newid": vm["vmid"],
    "name": vm["name"],
    "storage": vm["storage"],
    "full": 1 if vm.get("full", True) else 0,
}

post(f"/nodes/{vm['node']}/qemu/{vm['template_vmid']}/clone", clone_data)
print("✅ Clone operation submitted.")
