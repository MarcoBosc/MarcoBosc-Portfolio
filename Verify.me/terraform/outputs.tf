output "aws_lambda_name" {
  value = var.lambda_function_name
}

output "lambda_function" {
  value = var.function
}

output "aws_lambda_function_arn" {
  value = aws_lambda_function.lambda.arn
}