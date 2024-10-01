output "network_interface_id" {
  value = azurerm_network_interface.interface.id
}

output "snet1_id" {
  value       = azurerm_subnet.snet1.id
  description = "ID of the subnet1"
}