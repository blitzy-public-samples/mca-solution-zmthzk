output "instance_public_ips" {
  description = "Public IP addresses of deployed instances"
  value       = aws_instance.main[*].public_ip
}

output "database_connection_string" {
  description = "Connection string for the main database"
  value       = "postgresql://${aws_db_instance.main.username}:${aws_db_instance.main.password}@${aws_db_instance.main.endpoint}/${aws_db_instance.main.name}"
  sensitive   = true
}

output "storage_bucket_names" {
  description = "Names of the created storage buckets"
  value       = aws_s3_bucket.main[*].id
}

output "api_endpoint_url" {
  description = "URL of the main API endpoint"
  value       = aws_api_gateway_stage.main.invoke_url
}

# HUMAN ASSISTANCE NEEDED
# The following block assumes the existence of a KMS key for encryption.
# Please verify the correct KMS key ARN is used and adjust as necessary.
output "service_account_key" {
  description = "Encrypted service account key"
  value       = aws_iam_access_key.service_account.encrypted_secret
  sensitive   = true
}

output "kms_key_arn" {
  description = "ARN of the KMS key used for encryption"
  value       = aws_kms_key.main.arn
}