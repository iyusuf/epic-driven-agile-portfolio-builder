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
API_BASE = os.getenv("PROXMOX_API")
USER = os.getenv("PROXMOX_USER")
TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")
TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")

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

print("🔍 Fetching node info from Proxmox...")
nodes = fetch("/nodes")
node_name = nodes[0]["node"]
print(f"✅ Node: {node_name}")

print("\n📦 Discovering VM Templates...")
templates = fetch(f"/nodes/{node_name}/qemu")
template = next((t for t in templates if t.get("template") == 1), None)
template_info = {
    "vmid": template["vmid"],
    "name": template["name"]
} if template else {}

print("\n💾 Discovering Storage Pools...")
storages = fetch(f"/nodes/{node_name}/storage")
storage = next((s for s in storages if s["type"] in ["dir", "lvm", "zfspool"]), None)

print("\n🌐 Discovering Network Bridges...")
networks = fetch(f"/nodes/{node_name}/network")
bridge = next((n["iface"] for n in networks if "vmbr" in n.get("iface", "")), None)

# Final discovery result
discovery = {
    "node": node_name,
    "template": template_info,
    "storage": storage["storage"] if storage else None,
    "bridge": bridge
}

# Write to JSON file
output_path = os.path.join(os.path.dirname(__file__), "explore.proxmox.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as f:
    json.dump(discovery, f, indent=2)

print("\n🧾 Discovery saved to explore.proxmox.json")
