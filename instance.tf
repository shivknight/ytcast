resource "aws_instance" "ytcast" {
  ami                         = "${data.aws_ami.amazon-linux-2.id}"
  instance_type               = "${var.instance_type}"
  key_name                    = "${var.key_name}"
  subnet_id                   = "${var.subnet_id}"
  vpc_security_group_ids      = "${var.security_group_ids}"
  associate_public_ip_address = false
}
