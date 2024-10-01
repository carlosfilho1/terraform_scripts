locals {
  location_map = {
    0 = "eastus"
    1 = "westus"
    2 = "westeurope"
  }

  # Validação de entrada
  selected_location = contains(keys(local.location_map), var.user_selected_location) ? local.location_map[tonumber(var.user_selected_location)] : var.user_selected_location
}


resource "azurerm_virtual_network" "labnet" {
  name                = var.name
  location            = local.selected_location
  resource_group_name = var.rg_name
  address_space       = var.address_space
  dns_servers         = var.dns_servers
}

resource "azurerm_subnet" "snet1" {
  name                 = "subnet1"
  resource_group_name  = azurerm_virtual_network.labnet.resource_group_name
  virtual_network_name = azurerm_virtual_network.labnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_subnet" "snet2" {
  name                 = "subnet2"
  resource_group_name  = azurerm_virtual_network.labnet.resource_group_name
  virtual_network_name = azurerm_virtual_network.labnet.name
  address_prefixes     = ["10.0.2.0/24"]
}


resource "azurerm_public_ip" "publicip" {
  name                = "public-ip"
  location            = azurerm_virtual_network.labnet.location
  resource_group_name = azurerm_virtual_network.labnet.resource_group_name
  allocation_method   = "Dynamic"  # ou "Static", dependendo da necessidade
  sku                 = "Basic"    # ou "Standard"
}


resource "azurerm_network_interface" "interface" {
  name                = "interface01"
  location            = azurerm_virtual_network.labnet.location
  resource_group_name = azurerm_virtual_network.labnet.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.snet1.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.publicip.id
  }
}