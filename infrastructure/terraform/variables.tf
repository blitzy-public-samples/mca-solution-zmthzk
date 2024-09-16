# Project-specific variables
variable "project_id" {
  description = "The ID of the GCP project"
  type        = string
}

variable "region" {
  description = "The region to deploy resources"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The zone to deploy resources"
  type        = string
  default     = "us-central1-a"
}

# Resource naming and sizing variables
variable "instance_name_prefix" {
  description = "Prefix for instance names"
  type        = string
  default     = "app-instance"
}

variable "instance_machine_type" {
  description = "Machine type for instances"
  type        = string
  default     = "n1-standard-1"
}

variable "db_instance_name" {
  description = "Name for the database instance"
  type        = string
  default     = "app-db-instance"
}

variable "db_instance_tier" {
  description = "The machine type to use for the database instance"
  type        = string
  default     = "db-f1-micro"
}

# Configuration options for various GCP services
variable "enable_cloud_storage" {
  description = "Whether to enable Cloud Storage"
  type        = bool
  default     = true
}

variable "enable_cloud_sql" {
  description = "Whether to enable Cloud SQL"
  type        = bool
  default     = true
}

variable "enable_cloud_run" {
  description = "Whether to enable Cloud Run"
  type        = bool
  default     = false
}

variable "vpc_network_name" {
  description = "Name of the VPC network"
  type        = string
  default     = "app-network"
}

variable "subnet_cidr" {
  description = "CIDR range for the subnet"
  type        = string
  default     = "10.0.0.0/24"
}

# Environment-specific variables
variable "environment" {
  description = "The environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "min_instances" {
  description = "Minimum number of instances in the instance group"
  type        = map(number)
  default = {
    dev     = 1
    staging = 2
    prod    = 3
  }
}

variable "max_instances" {
  description = "Maximum number of instances in the instance group"
  type        = map(number)
  default = {
    dev     = 2
    staging = 4
    prod    = 10
  }
}

variable "db_backup_enabled" {
  description = "Whether to enable database backups"
  type        = map(bool)
  default = {
    dev     = false
    staging = true
    prod    = true
  }
}

variable "db_backup_start_time" {
  description = "Start time for database backups (HH:MM format)"
  type        = string
  default     = "02:00"
}

# HUMAN ASSISTANCE NEEDED
# The following variables might need adjustment based on specific project requirements
variable "additional_tags" {
  description = "Additional tags to apply to resources"
  type        = map(string)
  default     = {}
}

variable "custom_vpc_config" {
  description = "Custom VPC configuration"
  type        = map(string)
  default     = {}
}