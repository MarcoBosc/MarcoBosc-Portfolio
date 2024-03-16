resource "aws_iam_role" "lambda_role" { # assume role para o lambda
  name = var.lambda_assume_role

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "bucket_policy" {
  name        = var.s3_policy_name
  description = "Permite que o lambda crie objetos em um bucket"
  policy      = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowLambdaToPutObjectOnS3",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::*/*"
      ]
    }
  ]
}
EOF
}

resource "aws_lambda_function" "lambda" { 
  function_name    = "${var.lambda_function_name}-lambda"
  role             = aws_iam_role.lambda_role.arn
  handler          = var.lambda_handler
  runtime          = var.lambda_runtime
  filename         = var.lambda_file_name
  source_code_hash = filebase64sha256(var.lambda_file_name)
}

resource "aws_iam_policy_attachment" "lambda_bucket_policy_attachment" { # atrela a política que permite o lambda criar objetos no s3
  name       = "lambda-s3-policy-attachment"
  roles      = [aws_iam_role.lambda_role.name]
  policy_arn = aws_iam_policy.bucket_policy.arn
}