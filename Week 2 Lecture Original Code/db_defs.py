#  LECTURE

from google.appengine.ext import ndb
from google.appengine.ext import blobstore

class Message(ndb.Model):
    channel = ndb.StringProperty(required=True)
    date_time = ndb.DateTimeProperty(required=True)
    count = ndb.IntegerProperty(required=True)

class Channel(ndb.Model):
    name = ndb.StringProperty(required=True)
    classes = ndb.KeyProperty(repeated=True)
    active = ndb.BooleanProperty(required=True)
    #icon = ndb.BlobProperty(required=False)
    icon = blobstore.BlobKey

class ChannelClass(ndb.Model):
    name = ndb.StringProperty(required=True)
