
variable "location" {
    default = "eastus"
  }

  variable "rg_name" {
    default = "tf-project3-rg"
    
  }

  variable "acr_name" {
    default = "terraformversion3"
  }

  variable "aks_name" {
    default = "terra-aks-cluster"
  }

  variable "node_count" {
  default = 1
}

variable "node_size" {
  default = "standard_d2s_v3"
}