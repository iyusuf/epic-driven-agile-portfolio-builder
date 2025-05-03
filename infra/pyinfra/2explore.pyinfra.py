# File: infra/pyinfra/explore.pyinfra.py

import os
import requests
import json
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress SSL warnings for self-signed certs
urllib3.disable_warnings(InsecureRequestWarning)

# Load .env file
load_dotenv()

# Load Proxmox API details from environment
API_BASE = os.getenv("PROXMOX_API")  # e.g., "https://192.168.55.201:8006/api2/json"
USER = os.getenv("PROXMOX_USER")      # e.g., "iyusuf@pam"
TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")  # e.g., "bpg"
TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")  # e.g., "a4453a..."

if not API_BASE or not USER or not TOKEN_ID or not TOKEN_SECRET:
    raise ValueError("❌ Environment variables PROXMOX_API, PROXMOX_USER, PROXMOX_TOKEN_ID, and PROXMOX_TOKEN_SECRET must be set.")

HEADERS = {
    "Authorization": f"PVEAPIToken={USER}!{TOKEN_ID}={TOKEN_SECRET}"
}

def fetch(endpoint):
    url = f"{API_BASE}{endpoint}"
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    return response.json()["data"]

# --- Node Info ---
print("🔍 Fetching node info from Proxmox...")
nodes = fetch("/nodes")
print("✅ Available Nodes:")
for node in nodes:
    print(f"  - {node['node']} (Status: {node['status']})")

node_name = nodes[0]["node"]

# --- Template Discovery ---
print("\n📦 Available VM Templates:")
templates = fetch(f"/nodes/{node_name}/qemu")
for tmpl in templates:
    if tmpl.get("template") == 1:
        print(f"  - VMID: {tmpl['vmid']} → {tmpl['name']}")

# --- Storage Pools ---
print("\n💾 Available Storage Pools:")
storages = fetch(f"/nodes/{node_name}/storage")
for storage in storages:
    print(f"  - {storage['storage']} ({storage['type']})")

# --- Network Bridges ---
print("\n🌐 Available Network Bridges:")
networks = fetch(f"/nodes/{node_name}/network")
for net in networks:
    if 'vmbr' in net.get('iface', ''):
        print(f"  - {net['iface']}")

# --- Summary block ---
print("\n🧾 Discovery complete.")