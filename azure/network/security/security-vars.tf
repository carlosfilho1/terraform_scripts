variable "name" {
    default = "Lab"
    type = string
    description = "(optional) describe your variable"
}

variable "location" {
    default = "East US"
    type = string
    description = "(optional) describe your variable"
}

variable "resource_group" {
  default = "lab"
  type = string
  description = "(optional) describe your variable"
}

variable "user_selected_location" {
  description = "Localização escolhida pelo usuário"
  type        = string
}
