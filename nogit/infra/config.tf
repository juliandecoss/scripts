terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
    local = {
      source = "hashicorp/local"
    }
    tls = {
      source = "hashicorp/tls"
    }
  }
}

provider "aws" {
  region     = "us-west-2"
  access_key = "AKIATNNPV2NMF73H2U7L"
  secret_key = "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"
}

terraform {
  backend "local" {
    path = "/Users/intern/Desktop/infra/.terraform/terraform.tfstate"
  }
}
