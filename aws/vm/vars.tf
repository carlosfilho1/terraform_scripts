variable "vm_instance" {
  default = "t2.micro"
}

variable "vm_name" {
  default = "lab-qa"
}

variable "vm_image" {
  default = "ami-04a98573e58903ee0" # Ubuntu 22.04 LTS
}

variable "access_key" {
  type = string
}

variable "secret_key" {
  type = string
}