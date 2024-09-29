terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.68.0"
    }
  }
}

# Definindo o provedor AWS
provider "aws" {
  region  = var.region
  profile = "default"
}


resource "aws_s3_bucket" "simple_bucket" {
  bucket = var.aws_s3_bucket
    tags = {
    Name        = "bucket"
    Environment = "projeto_aula_terraform"
  }
}

resource "aws_s3_bucket_accelerate_configuration" "simple" {
  bucket = aws_s3_bucket.simple_bucket.id
  status = "Enabled"
}

resource "aws_s3_bucket_ownership_controls" "simple" {
  bucket = aws_s3_bucket.simple_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "simple" {
  bucket = aws_s3_bucket.simple_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "simple" {
  depends_on = [
    aws_s3_bucket_ownership_controls.simple,
    aws_s3_bucket_public_access_block.simple,
  ]

  bucket = aws_s3_bucket.simple_bucket.id
  acl    = "public-read"
}