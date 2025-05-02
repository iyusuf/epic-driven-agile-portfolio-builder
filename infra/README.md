# ⚙️ Phase 0: Infrastructure Readiness for Development 🐳

![Phase Status](https://img.shields.io/badge/Phase%200-In%20Progress-yellow)

**Goal:** Establish a developer-friendly, locally runnable infrastructure foundation to support all future application epics. This includes provisioning, container orchestration, developer bootstrap scripts, and CI/CD enablers.

---

## 📑 Table of Contents

* [Start Here Checklist](#-start-here-checklist)
* [Epic 0.1: Provision and Bootstrap Local Dev Infrastructure](#-epic-01-provision-and-bootstrap-local-dev-infrastructure-)
* [Epic 0.2: Local Container Stack and Developer Bootstrap](#-epic-02-local-container-stack-and-developer-bootstrap-)
* [Epic 0.3: DevOps Readiness and Git Integration](#-epic-03-devops-readiness-and-git-integration-)

---

### ✅ Start Here Checklist

* [ ] Set up a GitHub repo: `dev-sandbox-bootstrap`
* [ ] Clone and configure Terraform for Proxmox access
* [ ] Prepare `cloud-init` scripts for OS bootstrapping
* [ ] Create developer lifecycle scripts: `dev-up.sh` and `dev-down.sh`
* [ ] Deploy and test Docker Swarm across VMs
* [ ] Configure Traefik with nip.io for local DNS
* [ ] Launch local container registry for internal use
* [ ] Push initial commit and tag `phase0-ready`

---

### 🔹 Epic 0.1: Provision and Bootstrap Local Dev Infrastructure 🐳

| #     | **User Story**                             | **Goal**                                                 | **Primary Tools**                       | **Target Outcome**                             |
| ----- | ------------------------------------------ | -------------------------------------------------------- | --------------------------------------- | ---------------------------------------------- |
| 0.1.1 | Provisioning VMs with Terraform on Proxmox | Automate Ubuntu VM provisioning for a repeatable sandbox | Terraform, Proxmox                      | Devs can spin up and tear down VMs from code   |
| 0.1.2 | Base OS Setup with Cloud-Init              | Install Docker, git, Python, Node.js via cloud-init      | Cloud-init, bash                        | VMs are developer-ready at first boot          |
| 0.1.3 | PostgreSQL on Dedicated VM                 | Move stateful DB from container to KVM/QEMU-hosted VM    | PostgreSQL, Proxmox, Ansible (optional) | Persistent DB aligned with production topology |

### 🔹 Epic 0.2: Local Container Stack and Developer Bootstrap 🐳

| #     | **User Story**                          | **Goal**                                                        | **Primary Tools**               | **Target Outcome**                                     |
| ----- | --------------------------------------- | --------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------ |
| 0.2.1 | Docker Swarm Cluster Bootstrapping      | Prepare 1 manager + 2 worker nodes for container workloads      | Docker Swarm, Shell             | Local container orchestration with service discovery   |
| 0.2.2 | Local DNS Routing with Traefik + nip.io | Enable human-friendly service URLs like `api.nip.io`            | Traefik, Docker Compose, nip.io | Easier API debugging and front-end to back-end routing |
| 0.2.3 | Developer Sandbox CLI Tool              | Enable devs to run `dev-up.sh` and `dev-down.sh` for full stack | Bash, make, Docker Compose      | One-line developer environment setup                   |

### 🔹 Epic 0.3: DevOps Readiness and Git Integration 🐳

| #     | **User Story**                    | **Goal**                                     | **Primary Tools**         | **Target Outcome**                                                |
| ----- | --------------------------------- | -------------------------------------------- | ------------------------- | ----------------------------------------------------------------- |
| 0.3.1 | GitOps-Friendly Repo Structure    | Standard folder structure + Makefiles + Docs | Git, Markdown             | Onboard new devs via GitHub and documentation                     |
| 0.3.2 | Secure Private Container Registry | Setup internal Docker registry for images    | Harbor or GitLab Registry | Developers can push/pull locally with no public access dependency |
