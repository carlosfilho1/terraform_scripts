resource "azurerm_network_security_group" "labsec" {
  name                = var.name
  location            = var.user_selected_location
  resource_group_name = var.resource_group
}

resource "azurerm_network_security_rule" "ssh_rule" {
  name                        = "AllowInternetOutbound"
  priority                    = 300
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_network_security_group.labsec.resource_group_name
  network_security_group_name = azurerm_network_security_group.labsec.name
}
