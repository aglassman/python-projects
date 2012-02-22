import webapp2
import jinja2
import os
from google.appengine.api import mail

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
        def get(self):
                template_values = {
						'menuOptions':[{'url':'/','text':'Welcome','selected':True},
							{'url':'/dateAndLocation','text':'Date & Location'},
							{'url':'/accomadations','text':'Accomadations'}],
				        'headerText': 'Amanda Marie McConnell & Andrew Leon Glassman'
				}
                template = jinja_environment.get_template('templates/welcome.html')
                self.response.out.write(template.render(template_values))

class DatePage(webapp2.RequestHandler):
        def get(self):
                template_values = {
						'menuOptions':[{'url':'/','text':'Welcome'},
							{'url':'/dateAndLocation','text':'Date & Location','selected':True},
							{'url':'/accomadations','text':'Accommodations'}],
				        'headerText': 'Amanda Marie McConnell & Andrew Leon Glassman'
				}
                template = jinja_environment.get_template('templates/dateAndLocation.html')
                self.response.out.write(template.render(template_values))

class AccomadationPage(webapp2.RequestHandler):
        def get(self):
                template_values = {
						'menuOptions':[{'url':'/','text':'Welcome'},
							{'url':'/dateAndLocation','text':'Date & Location'},
							{'url':'/accomadations','text':'Accomadations','selected':True}],
				        'headerText': 'Amanda Marie McConnell & Andrew Leon Glassman'
				}
                template = jinja_environment.get_template('templates/accomodations.html')
                self.response.out.write(template.render(template_values))
				
app = webapp2.WSGIApplication([('/', MainPage),
								('/dateAndLocation', DatePage),
								('/accomadations', AccomadationPage)],debug=True)