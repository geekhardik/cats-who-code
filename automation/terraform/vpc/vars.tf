variable "aws_access_key" {}
variable "aws_secret_key" {}

variable "aws_region" {
  description = "EC2 Region for the VPC"
  default = "us-west-2"
}

variable "vpc_cidr" {
  description = "CIDR for the whole VPC"
  default = "10.0.0.0/16"
}

variable "us_west_2_azs" {
  description = "CIDRs for the Private Subnets"
  default = {
    a = "us-west-2a"
    b = "us-west-2b"
    c = "us-west-2c"
  }
}

variable "aws_nat_gateway_subnet" {
  description = "Public region for the Nat Gateway"
  default = "us-west-2"
}

variable "public_subnet_cidrs" {
  description = "CIDR for the Public Subnets"
  default = {
    a = "10.0.1.0/24"
    b = "10.0.2.0/24"
    c = "10.0.3.0/24"
  }
}

variable "private_subnet_cidrs" {
  description = "CIDRs for the Private Subnets"
  default = {
    a = "10.0.4.0/24"
    b = "10.0.5.0/24"
    c = "10.0.6.0/24"
  }
}

variable "amis" {
  description = "AMIs by region"
  default = {
    us-west-2 = "ami-bf4193c7"
  }
}
