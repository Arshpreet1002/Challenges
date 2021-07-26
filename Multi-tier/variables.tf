variable "namespace" {
  description = "The project namespace to use for unique resource naming"
  type        = string
}
variable "ssh_keypair" {
  description = "SSH keypair to use for EC2 instance"
  default     = null
  type        = string
}
variable "region" {
  description = "AWS region"
  default     = "us-west-2"
  type        = string
}
variable "db_config"{
  description = "db_details"
  default = "abc"
}
variable "vpc"{
  description = "vpc_details"
  default = "abc"
  type = any
}
variable "sg"{
  description = "sg_details"
  default = "abc"
  type = any
}
