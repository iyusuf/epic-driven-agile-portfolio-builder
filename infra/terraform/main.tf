terraform {
  required_providers {
    proxmox = {
      source  = "Telmate/proxmox"
      version = ">= 2.9.11"
    }
  }
}

provider "proxmox" {
  pm_api_url      = var.proxmox_api_url
  pm_api_token_id = var.proxmox_token_id
  pm_api_token_secret = var.proxmox_token_secret
  pm_tls_insecure = true
}

resource "proxmox_vm_qemu" "dev_vm" {
  count       = var.target_vm_count
  name        = "${var.vm_base_name}-${count.index + 1}"
  target_node = var.proxmox_node
  clone       = var.vm_template_name

  cores       = 2
  sockets     = 1
  memory      = 2048

  cloudinit_cdrom_storage = var.storage_pool
  sshkeys     = var.ssh_pubkey

  network {
    model     = "virtio"
    bridge    = var.bridge_name
  }

  disk {
    size      = "20G"
    type      = "scsi"
    storage   = var.storage_pool
    iothread  = true
  }

  os_type    = "cloud-init"
  agent      = 1
  ciuser     = "ubuntu"
  ipconfig0  = "ip=dhcp"
}