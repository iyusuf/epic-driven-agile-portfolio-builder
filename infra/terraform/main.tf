# ---------------------------------------------
# Terraform Backend (optional local state)
# ---------------------------------------------
terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = ">= 3.0.1-rc8"
    }
  }
  backend "local" {}
}

# ---------------------------------------------
# Provider Configuration
# ------------------v---------------------------
provider "proxmox" {
  pm_api_url          = var.pm_api_url
  pm_api_token_id     = var.pm_api_token_id
  pm_api_token_secret = var.pm_api_token_secret
  pm_tls_insecure     = true
}

# ---------------------------------------------
# Input Variables
# ---------------------------------------------
variable "pm_api_url" {
  default = "https://192.168.55.201:8006/api2/json"
}
variable "pm_api_token_id" {
  default = "iyusuf@pam!bpg"
}
variable "pm_api_token_secret" {
  default = "a4453aa8-de0f-4247-9387-3991fb027ae4"
}
variable "target_node" {
  default = "pve-tde"
}
variable "template_name" {
  default = "Ubuntu22-CI-Template"
}
variable "vm_name_prefix" {
  default = "devvm"
}
variable "vm_count" {
  default = 1
  type    = number
}
variable "vm_cores" {
  default = 2
  type    = number
}
variable "vm_memory" {
  default = 2048
  type    = number
}
variable "disk_size" {
  default = "10G"
  type    = string
}
variable "disk_storage" {
  default = "local-lvm"
}
variable "network_bridge" {
  default = "vmbr0"
}
variable "ssh_key_path" {
  default = "/home/iyusuf/.ssh/id_ed25519.pub"
}

# ---------------------------------------------
# VM Resource Definition
# ---------------------------------------------
resource "proxmox_vm_qemu" "vm" {
  count       = var.vm_count
  name        = format("%s-%02d", var.vm_name_prefix, count.index + 1)
  target_node = var.target_node
  clone       = var.template_name

  agent       = 1
  os_type     = "cloud-init"
  cores       = var.vm_cores
  memory      = var.vm_memory

  disk {
    type    = "scsi"
    storage = var.disk_storage
    size    = var.disk_size
  }
  network {
    model  = "virtio"
    bridge = var.network_bridge
  }

  ipconfig0 = "ip=dhcp"
  sshkeys   = file(var.ssh_key_path)

  lifecycle {
    ignore_changes = [network]
  }
}

# ---------------------------------------------
# Outputs (optional)
# ---------------------------------------------
output "vm_name" {
  value = proxmox_vm_qemu.vm[*].name
}
