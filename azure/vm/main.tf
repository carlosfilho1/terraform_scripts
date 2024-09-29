module "rg" {
  source  = "../resource-group"
  user_rg = var.user_rg
} 


module "network-vnet" {
  source                 = "../network/vnet"
  user_selected_location = var.user_selected_location
  depends_on             = [module.rg]
}

module "security" {
  source                 = "../network/security"
  user_selected_location = var.user_selected_location
  depends_on             = [module.rg]

}

resource "azurerm_subnet_network_security_group_association" "snet1_nsg_association" {
  subnet_id                 = module.network-vnet.snet1_id
  network_security_group_id = module.security.security_group_id
}

resource "azurerm_linux_virtual_machine" "ubuntu" {
  name                = "ubuntu-lab"
  resource_group_name = var.rg_name
  location            = var.user_selected_location
  size                = "Standard_F2"
  admin_username      = "adminuser"
  network_interface_ids = [
    module.network-vnet.network_interface_id
  ]

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}
