#  Assignment3
#  Micheal Willard
#  CS496 Oregon State University

import webapp2
from google.appengine.api import oauth
import datetime

app = webapp2.WSGIApplication([
    ('/player', 'player.Player'),
], debug=True)

app.router.add(webapp2.Route(r'/player/<id:[0-9]+><:/?>', 'player.Player'))
app.router.add(webapp2.Route(r'/player/search', 'player.PlayerSearch'))
#  Create a game
app.router.add(webapp2.Route(r'/game', 'game.Game'))
#  Get a specific game by ID
app.router.add(webapp2.Route(r'/game/<id:[0-9]+><:/?>', 'game.Game'))
#  Delete a game
app.router.add(webapp2.Route(r'/delete/game/<id:[0-9]+><:/?>', 'game.DelGame'))
#  Add player to attending
app.router.add(webapp2.Route(r'/a/game/<gid:[0-9]+>/player/<pid:[0-9]+><:/?>', 'game.Attending'))
#  Add player to not_attending
app.router.add(webapp2.Route(r'/na/game/<gid:[0-9]+>/player/<pid:[0-9]+><:/?>', 'game.NotAttending'))
