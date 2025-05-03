# 📘 Task Journal: Phase 0 — Infrastructure Readiness

This file logs task-level activities, decisions, and CLI outputs as a running record of work performed on Phase 0.

---

## 📅 2025-05-02

### ✅ Task: Set up dev sandbox shell scripts and Makefile
- Created `dev-up.sh` and `dev-down.sh` in `/infra/scripts/`
- Added `Makefile` to project root for standardized CLI
- Verified working locally with:
  ```bash
  make up
  make down
  ```

---

### ✅ Task: Scaffold Terraform infrastructure provisioning
- Generated `main.tf` with `${var.*}` placeholders
- Created `variables.tf` for Proxmox, VM, and networking inputs
- Plan to populate values via `terraform.tfvars` or `.env` next

---

### ✅ Task: Introduced debug logging
- Created `/infra/logs/phase0-debug-log.md`
- Logs from `make` and troubleshooting will be appended here

---

## ⏭️ Upcoming
- Run cURL commands to discover:
  - Proxmox node name
  - Template name
  - Storage pool
  - Network bridge
- Create `terraform.tfvars` to test `terraform plan`