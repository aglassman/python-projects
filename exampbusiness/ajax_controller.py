import jinja2
import os
import time

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def testRequest(request, *args, **kwargs):
		template = jinja_environment.get_template('templates/ajax.html')
		return template.render()
		
def testRequest2(request, *args, **kwargs):
		time.sleep(2)
		template_values = {'fname':'Andy', 'lname':'Glassman'}
		template = jinja_environment.get_template('templates/namepopup.html')
		return template.render(template_values)