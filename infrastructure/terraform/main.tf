# Main Terraform configuration file for provisioning Google Cloud Platform resources

# Provider configuration for Google Cloud
provider "google" {
  project = var.project_id
  region  = var.region
}

# Resource definitions for GCP services

# Compute Engine instance
resource "google_compute_instance" "app_server" {
  name         = "app-server"
  machine_type = "e2-medium"
  zone         = "${var.region}-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = file("startup-script.sh")

  tags = ["http-server", "https-server"]
}

# Cloud Storage bucket
resource "google_storage_bucket" "static_assets" {
  name     = "${var.project_id}-static-assets"
  location = var.region
}

# Firestore database
resource "google_firestore_database" "database" {
  project                 = var.project_id
  name                    = "(default)"
  location_id             = var.region
  type                    = "FIRESTORE_NATIVE"
  concurrency_mode        = "OPTIMISTIC"
  app_engine_integration_mode = "DISABLED"
}

# Network and security group configurations
resource "google_compute_firewall" "allow_http" {
  name    = "allow-http"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-server", "https-server"]
}

# Database and storage resource provisioning
# (Firestore and Cloud Storage already provisioned above)

# API and service account configurations
resource "google_project_service" "apis" {
  for_each = toset([
    "compute.googleapis.com",
    "storage-api.googleapis.com",
    "firestore.googleapis.com",
  ])
  
  service = each.key
  disable_on_destroy = false
}

resource "google_service_account" "app_service_account" {
  account_id   = "app-service-account"
  display_name = "App Service Account"
}

resource "google_project_iam_member" "app_service_account_roles" {
  for_each = toset([
    "roles/datastore.user",
    "roles/storage.objectAdmin",
  ])
  
  role    = each.key
  member  = "serviceAccount:${google_service_account.app_service_account.email}"
  project = var.project_id
}

# HUMAN ASSISTANCE NEEDED
# The following variables need to be defined in a separate variables.tf file:
# - var.project_id
# - var.region
# Please create a variables.tf file and define these variables with appropriate descriptions and default values if applicable.