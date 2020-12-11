#  Assignment3
#  Micheal Willard
#  CS496 Oregon State University

import webapp2
from google.appengine.ext import ndb
import db_models
import json
import datetime

#  Create a Player
class Player(webapp2.RequestHandler):

    def post(self):
        """Creates a Player entity

        POST Body Variables:
        name - Required. Player's name
        email - Required. email
        phone - phone number as a string
        password - Required.
        """
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        new_player = db_models.Player()
        name = self.request.get('name', default_value=None)
        email = self.request.get('email', default_value=None)
        phone = self.request.get('phone', default_value=None)
        password = self.request.get('password', default_value=None)
        # name is required, check if included
        if name:
            new_player.name = name
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, A player name is Required"
            return
        if name:
            new_player.password = password
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, A password is Required"
            return
        if email:
            new_player.email = email
        if phone:
            new_player.phone = phone
        key = new_player.put()
        out = new_player.to_dict()
        # dump the contents to json
        self.response.write(json.dumps(out))
        return
    def get(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports ap"
            return
        if 'id' in kwargs:
            player = ndb.Key(db_models.Player, int(kwargs['id'])).get()
            if not player:
                self.response.status = 404
                self.response.status_message = "Player Not Found"
                return
            out = ndb.Key(db_models.Player, int(kwargs['id'])).get().to_dict()
            self.response.write(json.dumps(out))
        else:
            # q = db_models.Player.query()
            # keys = q.fetch(keys_only=True)
            # results = { 'keys' : [x.id() for x in keys]}
            # self.response.write(json.dumps(results))

            rows = [row.to_dict() for row in db_models.Player.query()]
            self.response.write(json.dumps(rows))

class PlayerSearch(webapp2.RequestHandler):
    def post(self):
        """Search for Players

        POST Body Variables:
        name - string. Nickname
        email - string
        """
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        q = db_models.Player.query()
        if self.request.get('name',None):
            q = q.filter(db_models.Player.name == self.request.get('name'))
        if self.request.get('email',None):
            q = q.filter(db_models.Player.email == self.request.get('email'))
        keys = q.fetch(keys_only=True)
        results = { 'keys' : [x.id() for x in keys]}
        self.response.write(json.dumps(results))
