variable "lambda_handler" {
    default = "youtube.lambda_handler"
    type = string
}

variable "lambda_runtime" {
    default = "python3.8"
    type = string
}

variable "lambda_function_name" {
    default = "my-lambda-function"
    type = string
}

variable "layer_name" {
    default = "my-layer"
    type = string
}

provider "aws" {
    region = "us-west-2"
}

data "archive_file" "lambda_zip" {
    output_path = "youtube.zip"
    source_file = "youtube.py"
    type = "zip"
}

resource "aws_lambda_function" "this" {
    filename = data.archive_file.lambda_zip.output_path
    function_name = "my-lambda-function"
    handler = "youtube.lambda_handler"
    layers = [
        aws_lambda_layer_version.this.arn,
    ]
    role = aws_iam_role.this.arn
    runtime = "python3.8"
}

resource "aws_iam_policy" "this" {
    description = "Policy for lambda function"
    name = var.lambda_function_name
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
          {
            Action = "logs:*"
            Resource = "arn:aws:logs:*:*:*"
            Effect    = "Allow"
          }
        ]
      })
}

resource "aws_iam_role_policy_attachment" "this" {
    policy_arn = aws_iam_policy.this.arn
    role = aws_iam_role.this.name
}

resource "aws_lambda_function_url" "this" {
    authorization_type = "NONE"
    function_name = aws_lambda_function.this.function_name
}

resource "aws_lambda_layer_version" "this" {
    compatible_runtimes = [
        "python3.8",
    ]
    filename = "python.zip"
    layer_name = "my-lambda-layer"
}

resource "aws_iam_role" "this" {
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
          {
            Action = "sts:AssumeRole"
            Principal = {
              Service = "lambda.amazonaws.com"
            }
            Effect = "Allow"
          }
        ]
      })
    description = " Execution role for lambda function"
    name = var.lambda_function_name
}

output "lambda_function_url" {
    value = aws_lambda_function_url.this.function_url
}
