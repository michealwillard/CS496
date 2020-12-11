# LECTURE
import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Admin(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}

    def render(self, page):
        self.template_values['classes'] = [{'name':x.name, 'key':x.key.urlsafe()} for x in db_defs.ChannelClass.query(ancestor=ndb.Key(db_defs.ChannelClass, self.app.config.get('default-group'))).fetch()]
        self.template_values['channels'] = [{'name':x.name, 'key':x.key.urlsafe()} for x in db_defs.Channel.query(ancestor=ndb.Key(db_defs.Channel, self.app.config.get('default-group'))).fetch()]
        base_page.BaseHandler.render(self, page, self.template_values)

    def get(self):
        self.render('admin.html')

    def post(self, icon_key=None):
        action = self.request.get('action')
        if action == 'add_channel':
            #key: type + id
            k = ndb.Key(db_defs.Channel, self.app.config.get('default-group'))
            chan = db_defs.Channel(parent=k)
            chan.name = self.request.get('channel-name')
            chan.classes = [ndb.Key(urlsafe=x) for x in self.request.get_all('classes[]')]
            chan.active = True
            chan.icon = icon_key
            # put saves, returns to key
            chan.put()
            self.template_values['message'] = 'Added ' + chan.name + ' to the database.'
        elif action == 'add_class':
            k = ndb.Key(db_defs.ChannelClass, self.app.config.get('default-group'))
            c = db_defs.ChannelClass(parent=k)
            c.name = self.request.get('class-name')
            c.put()
            self.template_values['message'] = 'Added ' + c.name + ' to the database.'
        else:
            self.template_values['message'] = 'Action ' + action + ' is unknown.'
        #self.template_values['classes'] = db_defs.ChannelClass.query(ancestor=ndb.Key(db_defs.ChannelClass, self.app.config.get('default-group'))).fetch()
        self.render('admin.html')
