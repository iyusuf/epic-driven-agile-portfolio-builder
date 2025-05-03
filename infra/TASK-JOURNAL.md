## 📅 2025-05-03

### ✅ Task: Pyinfra Proxmox Node Discovery
- Ran `python provision.pyinfra.py`
- Successfully fetched node info from Proxmox API
- Node discovered: `pve-tde` (32 cores, 270GB RAM)
- Next: Add discovery logic for templates, storage, and bridges
- ✅ JSON response structure confirmed
- ⚠️ InsecureRequestWarning logged — will suppress in dev mode

## 📅 2025-05-03 (continued)

### ✅ Provision VM via Pyinfra & Proxmox API
- Added `dodo.py` orchestration file
- Validated `doit discover`, `provision`, and `postprovision`
- VM cloned from `AlmaLinux9-CI-Template`
- VM status confirmed via Proxmox + `provisioned-vms.json`


