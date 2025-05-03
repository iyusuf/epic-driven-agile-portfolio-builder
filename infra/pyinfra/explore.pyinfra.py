# File: iac/proxmox/pyinfra/explore.pyinfra.py

import os
import requests
import json
from dotenv import load_dotenv

# Load .env file from current directory or any parent folder
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
    return response.json()

print("🔍 Fetching node info from Proxmox...")
nodes = fetch("/nodes")
print(json.dumps(nodes, indent=2))