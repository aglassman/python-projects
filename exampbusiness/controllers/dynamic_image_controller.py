from services import dynamicImageServer
import webapp2

def getImage(request,jinja_environment, *args, **kwargs):
		return {'Content-Type':'image/jpeg', 'response': dynamicImageServer.getImage(request.route_kwargs['key'])}