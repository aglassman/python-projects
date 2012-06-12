import webapp2
import jinja2
import os
from google.appengine.api import mail

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

sidebarContent = [
											{'title': 'Web Technologies','body': 'HTML5, JavaScript, JQuery, CSS, JSP, Struts, Tiles, Spring WebMVC, Webapp2'},
											{'title': 'Servers','body': 'Weblogic, Tomcat, Liferay, Google App Engine'},
											{'title': 'Backend Technologies','body': 'Oracle, MySQL, Google Datastore, JDO, JPA, Hibernate, SQL , Map-Reduce'},
											{'title': 'Languages','body': 'Java,C#,Python,Javascript'},
											{'title': 'Other','body': 'XNA 4.0'}
										  ]

class MainPage(webapp2.RequestHandler):
        def get(self):
                template_values = {
						'menuOptions':[{'url':'/','text':'Home','selected':True},
										{'url':'/contact','text':'Contact Info'},
										{'url':'/packages','text':'Web Design Packages'},
										{'url':'/examples','text':'Design Examples'}],
				        'sidebarContent':sidebarContent,
				        'bodyContent' : '<p>Welcome,<br><br>My name is Andrew Glassman.  I am a software / web developer in the Milwaukee area.  I offer very affordable and professional web design. Please contact me via the \'Contact Info\' page if you are interested.  <br><br><i>Andrew Glassman</i></p>'
				}
                template = jinja_environment.get_template('templates/home.html')
                self.response.out.write(template.render(template_values))
				
class Contact(webapp2.RequestHandler):
        def get(self):
                template_values = {}
                template = jinja_environment.get_template('templates/codebrew/Contact.html')
                self.response.out.write(template.render(template_values))

class About(webapp2.RequestHandler):
        def get(self):
                template_values = {}
                template = jinja_environment.get_template('templates/codebrew/About.html')
                self.response.out.write(template.render(template_values))

class ExtraStuff(webapp2.RequestHandler):
        def get(self):
                template_values = {}
                template = jinja_environment.get_template('templates/codebrew/ExtraStuff.html')
                self.response.out.write(template.render(template_values))

class Projects(webapp2.RequestHandler):
        def get(self):
                template_values = {}
                template = jinja_environment.get_template('templates/codebrew/Projects.html')
                self.response.out.write(template.render(template_values))

class EmailMe(webapp2.RequestHandler):
        def post(self):
                mail.send_mail(sender="gmail.com ContactMe <andrew.glassman@gmail.com>",
								to="andrew.glassman@gmail.com",
								subject=self.request.get('replyTo') + " has sent you a message: " + self.request.get('subject'),
								body=self.request.get('body')+"--from: " + self.request.get('replyTo'))
                self.redirect('/contact')

class Packages(webapp2.RequestHandler):
        def get(self):
                template_values = {'menuOptions':[
									{'url':'/','text':'Home'},
									{'url':'/contact','text':'Contact Info'},
									{'url':'/packages','text':'Web Design Packages','selected':True},
									{'url':'/examples','text':'Design Examples'}]}
                template = jinja_environment.get_template('templates/packages.html')
                self.response.out.write(template.render(template_values))
				
class Examples(webapp2.RequestHandler):
        def get(self):
                template_values = {'menuOptions':[
									{'url':'/','text':'Home'},
									{'url':'/contact','text':'Contact Info'},
									{'url':'/packages','text':'Web Design Packages'},
									{'url':'/examples','text':'Design Examples','selected':True}]}
                template = jinja_environment.get_template('templates/examples.html')
                self.response.out.write(template.render(template_values))

class Index(webapp2.RequestHandler):
        def get(self):
                template_values = {}
                template = jinja_environment.get_template('templates/codebrew/index.html')
                self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', Index),
								('/contact',Contact),
								('/Contact.html',Contact),
								('/About.html',About),
								('/ExtraStuff.html',ExtraStuff),
								('/Projects.html',Projects),
								('/emailMe',EmailMe),
								('/packages',Packages),
								('/examples',Examples)],debug=True)