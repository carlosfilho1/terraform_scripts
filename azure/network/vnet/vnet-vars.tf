variable "name" {
  default     = "vnet"
  type        = string
  description = "(optional) O nome da Virtual Network"
}

variable "rg_name" {
  default     = "lab"
  type        = string
  description = "(optional) O nome do Resource Group"
}

variable "address_space" {
  default     = ["10.0.0.0/16"]
  type        = list(string)
  description = "(optional) O espaço de endereço da VNet"
}

variable "dns_servers" {
  default     = ["10.0.0.4", "10.0.0.5"]
  type        = list(string)
  description = "(optional) Servidores DNS"
}

variable "user_selected_location" {
  description = "Localização escolhida pelo usuário"
  type        = string
}