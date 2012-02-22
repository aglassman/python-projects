import webapp2

class EchoHandler(webapp2.RequestHandler):
        def get(self):
        	    print 'hi'
                self.response.out.write(self.request.arguments())
        def post(self):
        	    print 'ji'
                self.response.out.write(self.request.arguments())


app = webapp2.WSGIApplication([('/', EchoHandler)],debug=True)