import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CurrentChatHome(webapp2.RequestHandler):
        def get(self):
                template_values = {'hi':'bye'}
                template = jinja_environment.get_template('templates/currentchat.html')
                self.response.out.write(template.render(template_values))


class CurrentChat(webapp2.RequestHandler):
        def get(self):
                self.response.headers['Content-Type'] = 'text/event-stream'
                self.response.out.write("Data: hi\n\n")

class Say(webapp2.RequestHandler):
        def post(self):
                template_values = {'hi':'bye'}
                template = jinja_environment.get_template('templates/currentchat.html')
                self.response.out.write(template.render(template_values))
				
app = webapp2.WSGIApplication([('/', CurrentChatHome),
								('/say', Say),
								('/currentchatsse',CurrentChat)],debug=True)