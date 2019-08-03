resource "aws_route53_record" "ytcast" {
  zone_id = "${var.shivknight_com_zone}"
  name = "${var.name}"
  type = "CNAME"
  records = ["${aws_s3_bucket.ytcast.website_endpoint}"]
}
