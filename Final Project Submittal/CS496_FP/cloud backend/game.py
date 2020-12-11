#  Assignment3
#  Micheal Willard
#  CS496 Oregon State University

import webapp2
from google.appengine.ext import ndb
import db_models
import json
from datetime import datetime

class Game(webapp2.RequestHandler):
    def post(self):
        """Creates a Game entity

        POST Body Variables:
        opp_name - Required. Name of Opponent
        date_time - Required.  Time of the game 2016-10-21 16:54:57.000000
        location - Required. Field location
        attending[] = Array of player ids for attending players
        not_attending[] - Array of player ids for attending players
        """
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        new_game = db_models.Game()
        opp_name = self.request.get('opp_name', default_value=None)
        #temp_date_time = self.request.get('date_time', default_value=None)
        #date_time = datetime.strptime(temp_date_time, '%Y-%m-%d %H:%M:%S')
        date = self.request.get('date', default_value=None)
        time = self.request.get('time', default_value=None)
        location = self.request.get('location', default_value=None)
        attending = self.request.get_all('attending[]', default_value=None)
        not_attending = self.request.get_all('not_attending[]', default_value=None)

        #  Check for required opponent, datetime and location
        if opp_name:
            new_game.opp_name = opp_name
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, Opponent Name is Required"
            return
        # if date_time:
        #     new_game.date_time = date_time
        # else:
        #     self.response.status = 400
        #     self.response.status_message = "Invalid request, Date Time is Required"
        if date:
            new_game.date = date
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, Date is Required"
            return
        if time:
            new_game.time = time
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, Date Time is Required"
            return
        if location:
            new_game.location = location
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, Location is Required"
            return

        if attending:
            for player in attending:
                new_game.attending.append(ndb.Key(db_models.Player, int(player)))
        if not_attending:
            for player in not_attending:
                new_game.not_attending.append(ndb.Key(db_models.Player, int(player)))
        key = new_game.put()
        out = new_game.to_dict()
        self.response.write(json.dumps(out))
        return
    #  GET request to view game details with id included, or all game ids
    def get(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        if 'id' in kwargs:
            game = ndb.Key(db_models.Game, int(kwargs['id'])).get()
            if not game:
                self.response.status = 404
                self.response.status_message = "Game Not Found"
                return
            out = ndb.Key(db_models.Game, int(kwargs['id'])).get().to_dict()
            self.response.write(json.dumps(out))
        else:
            rows = [row.to_dict() for row in db_models.Game.query()]
            self.response.write(json.dumps(rows))


# Delete a game
class DelGame(webapp2.RequestHandler):
    def delete(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        if 'id' in kwargs:
            check = ndb.Key(db_models.Game, int(kwargs['id'])).get()
            game = ndb.Key(db_models.Game, int(kwargs['id']))
            if not check:
                self.response.status = 404
                self.response.status_message = "Game Not Found"
                return
        game.delete()
        self.response.write(game)
        self.response.write("Was deleted.")

# Add a Player to attending
class Attending(webapp2.RequestHandler):
    def put(self, **kwargs):
        """Adds a player id to attending

            POST Body Variables:
            gid - game id
            pid - player id
        """
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        if 'gid' in kwargs:
            game = ndb.Key(db_models.Game, int(kwargs['gid'])).get()
            if not game:
                self.response.status = 404
                self.response.status_message = "Game Not Found"
                return
        if 'pid' in kwargs:
            player = ndb.Key(db_models.Player, int(kwargs['pid']))
            if not player:
                self.response.status = 404
                self.response.status_message = "Player Not Found"
                return
        if player in game.not_attending:
            game.not_attending.remove(player)
            game.put()
        if player not in game.attending:
            game.attending.append(player)
            game.put()
        self.response.write(json.dumps(game.to_dict()))
        return

# Add a Player to attending
class NotAttending(webapp2.RequestHandler):
    def put(self, **kwargs):
        """Adds a player id to attending

            POST Body Variables:
            gid - game id
            pid - player id
        """
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, API only supports application/json MIME type"
            return
        if 'gid' in kwargs:
            game = ndb.Key(db_models.Game, int(kwargs['gid'])).get()
            if not game:
                self.response.status = 404
                self.response.status_message = "Game Not Found"
                return
        if 'pid' in kwargs:
            player = ndb.Key(db_models.Player, int(kwargs['pid']))
            if not player:
                self.response.status = 404
                self.response.status_message = "Player Not Found"
                return
        if player in game.attending:
            game.attending.remove(player)
            game.put()
        if player not in game.not_attending:
            game.not_attending.append(player)
            game.put()
        self.response.write(json.dumps(game.to_dict()))
        return
