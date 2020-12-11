#  Assignment3
#  Micheal Willard

from google.appengine.ext import ndb

class Model(ndb.Model):
    def to_dict(self):
        d = super(Model, self).to_dict()
        d['key'] = self.key.id()
        return d

class Update(Model):
    date_time = ndb.DateTimeProperty(required=True)
    user_count = ndb.IntegerProperty(required=True)
    message_count = ndb.IntegerProperty(required=True)

class Channel(Model):
    name = ndb.StringProperty(required=True)
    topics = ndb.StringProperty(repeated=True)
    mods = ndb.KeyProperty(repeated=True)
    updates = ndb.StructuredProperty(Update, repeated=True)

    def to_dict(self):
        d = super(Channel,self).to_dict()
        d['mods'] = [m.id() for m in d['mods']]
        return d

class Mod(Model):
    nick = ndb.StringProperty(required=True)
    email = ndb.StringProperty()
    name = ndb.StringProperty()
