# Create a new custom vpc without the default subnets 
resource "google_computer_network" "vpc_network"{
    name = "my-vpc-network"
    auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet_us"{
    name            = "subnet_us"
    ip_cidr_range   = "10.0.1.0/24"
    region          = "us-central1"
    network         = google_compute_network.vpc_network.id
}
