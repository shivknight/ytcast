from datetime import datetime
import os

from rfeed import *
from xml.sax.saxutils import XMLGenerator
import mutagen
from pprint import pprint

def generate_xml():
  rss_items = []
  default_metadata = {
    "title"   : "Unknown title",
    "purl"    : "Unknown URL",
    "artist"  : "Unknown artist",
    "description"    : "No description",
    "pubDate"    : "Unknown publication date",
  }

  files = os.scandir('./podcasts')
  for f in files:
    metadata = mutagen.File(f)
    i = Item (
      title = metadata.get('title', default_metadata['title']),
      link = metadata.get('purl', default_metadata['purl']),
      author = metadata.get('artist', default_metadata['artist']),
      description = metadata.get('description', default_metadata['description']),
      pubDate = datetime.strptime(metadata.get('date', default_metadata['pubDate'])[0], '%Y%m%d')
    )
    rss_items.append(i)

  feed = Feed (
    title = "dibbibyte",
    link = "http://www.example.com/rss",
    description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
    language = "en-US",
    lastBuildDate = datetime.now(),
    items = rss_items
  )
  with open("podcasts.xml","w") as pcast_file:
    feed.publish(XMLGenerator(pcast_file))

generate_xml()
