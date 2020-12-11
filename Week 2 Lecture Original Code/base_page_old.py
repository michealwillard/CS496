# lecture

import webapp2
import os
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class HelloWorld(webapp2.RequestHandler):
    template_variables = {}
    
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('helloworld.html')
        self.response.write(template.render())

    def post(self):
        self.template_variables['form_content'] = {}
        template = JINJA_ENVIRONMENT.get_template('helloworld.html')
        for i in self.request.arguments():
            self.template_variables['form_content'][i] = self.request.get(i)
        self.response.write(template.render(self.template_variables))
