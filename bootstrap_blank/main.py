import webapp2
import jinja2
import os
from google.appengine.api import users

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MenuItem:
    def __init__(self,title,url,active):
        self.title = title
        self.url = url
        self.active = active

menu = {'home':MenuItem('Home','/',False), 'howto':MenuItem('How To','/howto',False)}

def checkLogin(requestHandler):
    user = users.get_current_user()
    if not user:
        requestHandler.redirect(users.create_login_url(requestHandler.request.uri))


class Home(webapp2.RequestHandler):
        def get(self):
                checkLogin(self)
                menu['home'].active = True
                menu['howto'].active = False
                template = jinja_environment.get_template('templates/home.html')
                self.response.out.write(template.render(menu=menu))

class HowTo(webapp2.RequestHandler):
        def get(self):
                checkLogin(self)
                menu['home'].active = False
                menu['howto'].active = True
                template = jinja_environment.get_template('templates/howto.html')
                self.response.out.write(template.render(menu=menu))

app = webapp2.WSGIApplication([('/', Home),
							   ('/howto',HowTo)],debug=True)