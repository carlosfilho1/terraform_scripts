terraform {
  required_version = ">=1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.68.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region     = "us-east-1"
  access_key = var.access_key
  secret_key = var.secret_key

  default_tags {
    tags = {
      owner      = "projeto_aula_terraform"
      managed-by = "equipe_terraform"
    }
  }
}

# Create a VPC
resource "aws_vpc" "laboratorio" {
  cidr_block = "10.0.0.0/16"
}


# chave SSH
resource "aws_key_pair" "deployer_key" {
  key_name   = "deployer_key"
  public_key = file("~/.ssh/keyaws.pub") # Caminho para a chave pública
}


resource "aws_instance" "ubuntu_vm" {
  instance_type = var.vm_instance
  ami           = var.vm_image
  key_name      = aws_key_pair.deployer_key.key_name
  # Security group para permitir o tráfego SSH
  vpc_security_group_ids = [aws_security_group.ssh_sg.id]

  tags = {
    name = var.vm_name
  }
}

# Criar um security group que permita SSH
resource "aws_security_group" "ssh_sg" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Permitir de qualquer IP (ou restrinja a um IP específico)
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
