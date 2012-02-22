from model import db_model
from google.appengine.ext import db

def getImage(key):
	product = db.get(key)
	if product.image:
		return product.image
	else:
		return 'no image'