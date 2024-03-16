variable "aws_region" {
  type        = string
  description = "region to create the resources"
  default = "us-east-1"
}

variable "aws_owner" {
  type        = string
  default     = "Marco Boschetti"
  description = "project owner"
}

variable "bucket_name" {
  type        = string
  default     = "Verify.me/terraform/main.tf"
  description = "backend bucket name"
}
