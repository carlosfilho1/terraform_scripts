variable "name" {
  default     = "lab"
  type        = string
  description = "(optional) describe your variable"
}

variable "location" {
  default     = "East US"
  type        = string
  description = "(optional) describe your variable"
}

variable "user_rg" {
  default = "lab"
  description = "rg"
  type        = string
}
