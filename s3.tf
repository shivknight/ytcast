resource "aws_s3_bucket" "podcasts" {
  bucket = "${lookup(var.tags, "Name")}"
  acl = "public-read"
  acl = "public-read"

  website {
    index_document = "podcast.xml"
    error_document = "error.html"
  }
}