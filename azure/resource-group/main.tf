resource "azurerm_resource_group" "laboratorio" {
  name     = var.user_rg
  location = var.location
}