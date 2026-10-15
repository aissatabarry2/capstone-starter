terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.30"
    }
  }
}

provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "kind-devops"
}

variable "namespace" {
  type    = string
  default = "capstone"
}

resource "kubernetes_namespace" "app" {
  metadata {
    name = var.namespace
  }
}

output "namespace" {
  value = kubernetes_namespace.app.metadata[0].name
}
