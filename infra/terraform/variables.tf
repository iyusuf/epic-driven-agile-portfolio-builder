variable "proxmox_api_url" {
  description = "Proxmox API endpoint"
  type        = string
}

variable "proxmox_token_id" {
  description = "Proxmox API token ID (user@pam!token)"
  type        = string
}

variable "proxmox_token_secret" {
  description = "Proxmox API token secret"
  type        = string
  sensitive   = true
}

variable "proxmox_node" {
  description = "Proxmox node name"
  type        = string
}

variable "vm_template_name" {
  description = "Name of the VM template to clone"
  type        = string
}

variable "target_vm_count" {
  description = "Number of VMs to create"
  type        = number
  default     = 3
}

variable "vm_base_name" {
  description = "Base name for VMs"
  type        = string
}

variable "bridge_name" {
  description = "Network bridge to attach to the VM"
  type        = string
}

variable "storage_pool" {
  description = "Storage pool name to allocate VM disk"
  type        = string
}

variable "ssh_pubkey" {
  description = "SSH public key to inject via cloud-init"
  type        = string
}