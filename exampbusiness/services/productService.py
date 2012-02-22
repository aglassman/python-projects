from model import db_model
from google.appengine.ext import db
from google.appengine.api import urlfetch

def getAll():
	return db_model.Product.all()
	
def add(arguments):
	imageprop = arguments.pop('image')
	newProduct = db_model.Product(**arguments)
	newProduct.image = db.Blob(str(imageprop))
	newProduct.put()
	
def getProductWithSku(sku):
	q = db_model.Product.all()
	q.filter("sku =",sku)
	return q
	
def getProductWithKey(key):
	return db_model.Product.get(key)