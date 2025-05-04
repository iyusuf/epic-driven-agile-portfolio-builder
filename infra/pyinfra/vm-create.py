# File: infra/pyinfra/create_vm.pyinfra.py

import os
import json
import requests
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from pathlib import Path

# Disable SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

class ProxmoxVMCloner:
    def __init__(self):
        # Load .env from current script directory (sibling file)
        env_path = Path(__file__).resolve().parent / ".env"
        load_dotenv(dotenv_path=env_path)

        # Map environment variables from .env with explanation
        host = os.getenv("PROXMOX_HOST")  # PROXMOX_HOST → e.g., 192.168.55.201
        self.api_base = f"https://{host}:8006/api2/json" if host else None

        self.user = os.getenv("PROXMOX_USER")             # Token owner
        self.token_id = os.getenv("PROXMOX_TOKEN_NAME")   # Token label
        self.token_secret = os.getenv("PROXMOX_TOKEN_SECRET")  # Token secret

        # Fail fast if anything is missing
        if not all([self.api_base, self.user, self.token_id, self.token_secret]):
            raise ValueError("❌ Missing one or more required environment variables.")

        self.headers = {
            "Authorization": f"PVEAPIToken={self.user}!{self.token_id}={self.token_secret}"
        }

    def post(self, endpoint, payload):
        url = f"{self.api_base}{endpoint}"
        response = requests.post(url, headers=self.headers, json=payload, verify=False)
        print(f"🔁 POST {url} → {response.status_code}")
        if response.content:
            print(response.text)
        response.raise_for_status()
        return response.json()

    def clone_from_json(self, json_path):
        with open(json_path) as f:
            vm = json.load(f)

        print(f"🚀 Cloning VM from template {vm['template_vmid']} → {vm['vmid']} ({vm['name']})")

        clone_data = {
            "newid": vm["vmid"],
            "name": vm["name"],
            "storage": vm["storage"],
            "full": 1 if vm.get("full", True) else 0,
        }

        self.post(f"/nodes/{vm['node']}/qemu/{vm['template_vmid']}/clone", clone_data)
        print("✅ Clone operation submitted.")


if __name__ == "__main__":
    cloner = ProxmoxVMCloner()
    cloner.clone_from_json("vm-create.json")
