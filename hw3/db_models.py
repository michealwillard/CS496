#  Assignment3
#  Micheal Willard
#  CS496 Oregon State University

from google.appengine.ext import ndb

class Model(ndb.Model):
    def to_dict(self):
        d = super(Model, self).to_dict()
        d['key'] = self.key.id()
        return d

class Game(Model):
    opp_name = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    # date = ndb.DateProperty(required=True)
    # time = ndb.TimeProperty(required=True)
    # date_time = ndb.DateTimeProperty(required=True)
    location = ndb.StringProperty(required=True)
    attending = ndb.KeyProperty(repeated=True)
    not_attending = ndb.KeyProperty(repeated=True)

    def to_dict(self):
        d = super(Game,self).to_dict()
        d['attending'] = [a.id() for a in d['attending']]
        d['not_attending'] = [n.id() for n in d['not_attending']]
        return d

class Player(Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    phone = ndb.StringProperty()
    password = ndb.StringProperty(required=True)
