def mainPageHandler(request,jinja_environment, *args, **kwargs):
		template_values = {
			'menuOptions':[{'url':'/','text':'Home','selected':True}],
			'bodyContent' : '<p>Business Example - Construction in Progress.<br><a href=\"http://andrewglassman.appspot.com\">Glassman Web Design</a></p>'
		}
		template = jinja_environment.get_template('templates/home.html')
		return template.render(template_values)