import webapp2
from google.appengine.ext import ndb
import db_models
import json

class Mod(webapp2.RequestHandler):

    def post(self):
        """Creates a Mod entity

        POST Body Variables:
        nick - Required. Nickname
        email - email
        name - Real Name
        """
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        new_mod = db_models.Mod()
        nick = self.request.get('nick', default_value=None)
        email = self.request.get('email', default_value=None)
        name = self.request.get('name', default_value=None)
        # nick is required
        if nick:
            new_mod.nick = nick
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, Nickname is Required"
        if email:
            new_mod.email = email
        if name:
            new_mod.name = name
        key = new_mod.put()
        out = new_mod.to_dict()
        # dump the contents to json
        self.response.write(json.dumps(out))
        return
    def get(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports ap"
            return
        if 'id' in kwargs:
            out = ndb.Key(db_models.Mod, int(kwargs['id'])).get().to_dict()
            self.response.write(json.dumps(out))
        else:
            q = db_models.Mod.query()
            keys = q.fetch(keys_only=True)
            results = { 'keys' : [x.id() for x in keys]}
            self.response.write(json.dumps(results))

class ModSearch(webapp2.RequestHandler):
    def post(self):
        """Search for Moderators

        POST Body Variables:
        nick - string. Nickname
        email - string
        """
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        q = db_models.Mod.query()
        if self.request.get('nick',None):
            q = q.filter(db_models.Mod.nick == self.request.get('nick'))
        if self.request.get('email',None):
            q = q.filter(db_models.Mod.nick == self.request.get('email'))
        keys = q.fetch(keys_only=True)
        results = { 'keys' : [x.id() for x in keys]}
        self.response.write(json.dumps(results))
