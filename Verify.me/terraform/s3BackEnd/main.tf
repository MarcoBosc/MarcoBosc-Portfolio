terraform {

  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.73.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      owner      = var.aws_owner
      managed-by = "terraform"
    }
  }
}