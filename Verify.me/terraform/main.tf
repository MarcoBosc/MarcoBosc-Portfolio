terraform {

  required_version = ">= 1.0.0"

  backend "s3" {
    bucket = "verify-me-infra-remote-state-bucket" # Substitua pelo nome do seu Bucket
    key    = "verify-me-infra-modules-lambda-terraform/verify-me-infra-lambda-create-lambda.tfstate"
    region = "us-east-1"
  }

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