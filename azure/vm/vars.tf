variable "rg_name" {
  type        = string
  default     = "Lab"
  description = "Nome do grupo de recursos."
}

variable "rg_location" {
  default = "East US"
  description = "Selecione uma das localizações [0]East US [1]West Europe [2]East Asia"
  type        = string
}

variable "vm_name" {
  description = "Nome da máquina virtual"
  type        = string
}

variable "vnet_name" {
  type        = string
  default     = "laboranet"
  description = "(optional) describe your variable"
}

variable "vnet_address_space" {
  type        = list(string)
  default     = ["10.0.0.0/16"]
  description = "(optional) describe your variable"
}

variable "vnet_dns_servers" {
  type        = list(string)
  default     = ["10.0.0.4", "10.0.0.5"]
  description = "(optional) describe your variable"
}

variable "sec_name" {
  type        = string
  default     = "lab_security"
  description = "(optional) describe your variable"
}

variable "subscription_id" {
  default = "value"
  type    = string
}

variable "user_selected_location" {
  description = "Localização escolhida pelo usuário"
  type        = string
}

variable "user_rg" {
  default = "lab"
  description = "rg"
  type        = string
}