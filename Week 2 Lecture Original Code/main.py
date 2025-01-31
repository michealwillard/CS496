# lecture
import webapp2

config = {'default-group':'base-data'}

application = webapp2.WSGIApplication([
    ('/edit/channel', 'edit_channel.EditChannel'),
    ('/edit', 'edit.Edit'),
    ('/channel/add', 'add_channel.AddChannel'),
    ('/admin', 'admin.Admin'),
    ('/', 'base_page.HelloWorld'),
], debug=True, config=config)
