variable "key_name" {
  default = "mba"
}
variable "instance_type" {
  default = "t2.nano"
}
variable "vpc_id" {
  default = "vpc-7c6cfd1b"
}
variable "subnet_id" {
  default = "subnet-95f88af0"
}

variable "security_group_ids" {
  default = [
    "sg-000f1e77"
  ]
}

variable "tags" {
  default = {
    Name = "ytcast"
  }
}
