from google.appengine.ext import db

class Product(db.Model):
	sku = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	price = db.StringProperty(required =True)
	description = db.TextProperty(required=True)
	image = db.BlobProperty()