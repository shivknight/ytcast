from datetime import datetime
import os

from rfeed import *
import mutagen
from pprint import pprint

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

#item1 = Item(
#    title = "First article",
#    link = "http://www.example.com/articles/1",
#    description = "This is the description of the first article",
#    author = "Santiago L. Valdarrama",
#    guid = Guid("http://www.example.com/articles/1"),
#    pubDate = datetime.datetime(2014, 12, 29, 10, 00))
#
#item2 = Item(
#    title = "Second article",
#    link = "http://www.example.com/articles/2",
#    description = "This is the description of the second article",
#    author = "Santiago L. Valdarrama",
#    guid = Guid("http://www.example.com/articles/2"),
#    pubDate = datetime.datetime(2014, 12, 30, 14, 15))
#
feed = Feed (
  title = "dibbibyte",
  link = "http://www.example.com/rss",
  description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
  language = "en-US",
  lastBuildDate = datetime.now(),
  items = rss_items
)

print(feed.rss())
