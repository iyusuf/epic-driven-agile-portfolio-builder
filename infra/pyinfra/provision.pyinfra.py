# provision.pyinfra.py

from pyinfra import host
from pyinfra.operations import server
import os
import requests

# Load Proxmox credentials from environment
PROXMOX_API_URL = os.getenv("PROXMOX_API_URL")
PROXMOX_TOKEN_ID = os.getenv("PROXMOX_TOKEN_ID")
PROXMOX_TOKEN_SECRET = os.getenv("PROXMOX_TOKEN_SECRET")
HEADERS = {
    "Authorization": f"PVEAPIToken={PROXMOX_TOKEN_ID}={PROXMOX_TOKEN_SECRET}"
}

def fetch(endpoint):
    url = f"{PROXMOX_API_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    return response.json()["data"]

# Discover available nodes
nodes = fetch("/nodes")
print("✅ Available Proxmox Nodes:")
for node in nodes:
    print(f"  - {node['node']} (Status: {node['status']})")

# Discover available templates
templates = fetch(f"/nodes/{nodes[0]['node']}/qemu")
print("\n📦 Available VM Templates:")
for tmpl in templates:
    if tmpl.get('template') == 1:
        print(f"  - {tmpl['vmid']} → {tmpl['name']}")

# Discover storage pools
storages = fetch(f"/nodes/{nodes[0]['node']}/storage")
print("\n💾 Storage Pools:")
for store in storages:
    print(f"  - {store['storage']} ({store['type']})")

# Discover network bridges
networks = fetch(f"/nodes/{nodes[0]['node']}/network")
print("\n🌐 Network Bridges:")
for net in networks:
    if 'bridge' in net.get('iface', ''):
        print(f"  - {net['iface']}")

# --- Below this, VM provisioning would go using Proxmox HTTP POST ---
# Placeholder for future VM create commands via API