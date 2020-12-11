

import webapp2
from google.appengine.api import oauth

app = webapp2.WSGIApplication([
    ('/mod', 'mod.Mod'),
], debug=True)

app.router.add(webapp2.Route(r'/mod/<id:[0-9]+><:/?>', 'mod.Mod'))
app.router.add(webapp2.Route(r'/mod/search', 'mod.ModSearch'))
app.router.add(webapp2.Route(r'/channel', 'channel.Channel'))
app.router.add(webapp2.Route(r'/channel/<id:[0-9]+><:/?>', 'channel.Channel'))
app.router.add(webapp2.Route(r'/delete/channel/<id:[0-9]+><:/?>', 'channel.DelChannel'))
app.router.add(webapp2.Route(r'/channel/<cid:[0-9]+>/mod/<mid:[0-9]+><:/?>', 'channel.ChannelMods'))
