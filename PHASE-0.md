# ⚙️ Phase 0: Infrastructure Readiness for Development 🐳

> 📌 This document is intended to be saved as `Phase0.md` and referenced from `LEARNING_TRACKER.md` as part of a milestone-based learning tracker.

---

## 🧠 Platform-Wide Vision & Goals

> 🤖 **Vision:** Build a platform that can eventually be operated by a Local LLM agent under Model Context Protocol (MCP), enabling developers to spin up infra on demand, compliantly, and securely, using natural language or domain requests.
>
> **Strategic Objectives:**
>
> * Groundwork for real-world agentic systems work
> * Provisioning and configuration as part of a platform engineering initiative to help a small team (5–10 developers) self-serve fully bootstrapped infrastructure with CI/CD and test automation
> * Rapid skeleton service generation directly from OpenAPI contracts, staying current with evolving change requests or new features arriving mid-sprint
> * Clean architecture conformance — automatically generating package structure and validation tests to ensure strict adherence to domain-driven design and architectural boundaries

---

### 📅 2025-05-03 — Strategic Checkpoint

**Discussion Summary:**

* Moved away from Terraform and Ansible to Pyinfra for simplicity.
* Initial Pyinfra progress was fast, but complexity crept in with resource tuning and multi-VM logic.
* Pyinfra became flexible but hard to manage and track as scope increased.
* Reaffirmed long-term goal: build MCP-compatible infrastructure agent.

**Conclusion:**

* ✅ Pyinfra + JSON + doit is **MCP- and Agentic AI-friendly** (flat, inspectable, Pythonic)
* ❌ Terraform/Ansible, while great for state and scale, would slow down agent compatibility and increase boilerplate.
* 🔄 Decision: stay on lightweight Python stack for now. Reintroduce Terraform **only if** modular state tracking becomes overwhelming.

---

## 📑 Table of Contents

* [🧠 Platform-Wide Vision & Goals](#-platform-wide-vision--goals)
* [📅 2025-05-03 — Strategic Checkpoint](#-2025-05-03--strategic-checkpoint)
* [✅ Start Here Checklist](#-start-here-checklist)
* [🔹 Epic 0.1: Provision and Bootstrap Local Dev Infrastructure 🐳](#-epic-01-provision-and-bootstrap-local-dev-infrastructure-)
* [🔹 Epic 0.2: Local Container Stack and Developer Bootstrap 🐳](#-epic-02-local-container-stack-and-developer-bootstrap-)
* [🔹 Epic 0.3: DevOps Readiness and Git Integration 🐳](#-epic-03-devops-readiness-and-git-integration-)

---

### ✅ Start Here Checklist

> ℹ️ *Note: The `Makefile` at project root simplifies the use of `dev-up.sh`, `dev-down.sh`, and future CI/CD or Swarm tasks. It is kept for developer convenience and is not tied to provisioning logic.*

*

---

### 🔹 Epic 0.1: Provision and Bootstrap Local Dev Infrastructure 🐳

| #     | **User Story**                                      | **Goal**                                                   | **Primary Tools**                       | **Target Outcome**                                                    |
| ----- | --------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------- |
| 0.1.1 | Provisioning VMs with Pyinfra                       | Automate Ubuntu VM provisioning for a repeatable sandbox   | Pyinfra + Proxmox API                   | Devs can spin up and tear down VMs using a single Python file         |
| 0.1.2 | Base OS Setup with Cloud-Init                       | Install Docker, git, Python, Node.js via cloud-init        | Cloud-init, bash                        | VMs are developer-ready at first boot                                 |
| 0.1.3 | Enhanced Cloud-Init with SSH & Resource Settings 🆕 | Inject SSH keys, hostname, and tune CPU/memory/disk per VM | Cloud-init, Proxmox API, Pyinfra        | Sandbox VMs are cloud-init ready with named identity and login access |
| 0.1.4 | PostgreSQL on Dedicated VM                          | Move stateful DB from container to KVM/QEMU-hosted VM      | PostgreSQL, Proxmox, Ansible (optional) | Persistent DB aligned with production topology                        |

---

### 🔹 Epic 0.2: Local Container Stack and Developer Bootstrap 🐳

| #     | **User Story**                          | **Goal**                                                        | **Primary Tools**               | **Target Outcome**                                     |
| ----- | --------------------------------------- | --------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------ |
| 0.2.1 | Docker Swarm Cluster Bootstrapping      | Prepare 1 manager + 2 worker nodes for container workloads      | Docker Swarm, Shell             | Local container orchestration with service discovery   |
| 0.2.2 | Local DNS Routing with Traefik + nip.io | Enable human-friendly service URLs like `api.nip.io`            | Traefik, Docker Compose, nip.io | Easier API debugging and front-end to back-end routing |
| 0.2.3 | Developer Sandbox CLI Tool              | Enable devs to run `dev-up.sh` and `dev-down.sh` for full stack | Bash, make, Docker Compose      | One-line developer environment setup                   |

---

### 🔹 Epic 0.3: DevOps Readiness and Git Integration 🐳

| #     | **User Story**                    | **Goal**                                     | **Primary Tools**         | **Target Outcome**                                                |
| ----- | --------------------------------- | -------------------------------------------- | ------------------------- | ----------------------------------------------------------------- |
| 0.3.1 | GitOps-Friendly Repo Structure    | Standard folder structure + Makefiles + Docs | Git, Markdown             | Onboard new devs via GitHub and documentation                     |
| 0.3.2 | Secure Private Container Registry | Setup internal Docker registry for images    | Harbor or GitLab Registry | Developers can push/pull locally with no public access dependency |
