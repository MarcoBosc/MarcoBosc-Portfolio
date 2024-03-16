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

variable "lambda_function_name" {
  type        = string
  description = "lambda function name"
}

variable "lambda_handler" {
  type        = string
  default     = "lambda_function.lambda_handler"
  description = "lambda handler name"
}

variable "lambda_runtime" {
  type        = string
  default     = "python3.9"
  description = "script language"
}

variable "lambda_file_name" {
  type        = string
  default     = "lambda_function.zip"
  description = "zip file name"
}

variable "s3_policy_name" {
  type        = string
  default     = "permission-lambda-to-s3-policy"
  description = "policy to write on s3 bucket name"
}

variable "lambda_assume_role" {
  type        = string
  default     = "lambda-assume-role"
  description = "lambda assume role name"
}

variable "function" {
  default = "Lambda for rekognition and textract"
}
