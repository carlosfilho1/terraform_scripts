module "rg" {
  source = "../resource-group"
}

module "network-vnet" {
  source                 = "../network/vnet"
  user_selected_location = var.user_selected_location
  depends_on             = [module.rg]
}


resource "azurerm_storage_account" "example" {
  name                     = var.SA
  resource_group_name      = module.rg.rg_name
  location                 = var.user_selected_location
  account_tier             = "Standard"
  account_replication_type = "GRS"
  account_kind             = var.type_SA

  tags = {
    environment = "staging"
  }
}
