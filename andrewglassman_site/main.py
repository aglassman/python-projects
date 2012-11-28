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

menu = { 'home':MenuItem('Home','/',False),
         'about':MenuItem('About Me','/about',False),
         'twitter':MenuItem('Twitter','twitter',False)}
user = None
loginurl = None

def updateUser():
    global user, loginurl
    user = users.get_current_user()
    if user:
        loginurl = users.create_logout_url("/")
    else:
        loginurl = users.create_login_url("/")


class Home(webapp2.RequestHandler):
    def get(self):
            global user, loginurl
            menu['home'].active = True
            menu['about'].active = False
            menu['twitter'].active = False
            updateUser()
            template = jinja_environment.get_template('templates/home.html')
            self.response.out.write(template.render(menu=menu,user=user,loginurl=loginurl))

class About(webapp2.RequestHandler):
    def get(self):
            global user, loginurl
            menu['home'].active = False
            menu['about'].active = True
            menu['twitter'].active = False
            updateUser()
            template = jinja_environment.get_template('templates/about.html')
            self.response.out.write(template.render(menu=menu,user=user,loginurl=loginurl))

class Twitter(webapp2.RequestHandler):
    def get(self):
            global user, loginurl
            menu['home'].active = False
            menu['about'].active = False
            menu['twitter'].active = True
            updateUser()
            template = jinja_environment.get_template('templates/twitter.html')
            self.response.out.write(template.render(menu=menu,user=user,loginurl=loginurl))

app = webapp2.WSGIApplication([('/', Home),
							   ('/about',About),
                               ('/twitter',Twitter)],debug=True)