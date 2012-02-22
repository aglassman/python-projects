from services import productService
from services import dynamicImageServer
import webapp2

def listProducts(request,jinja_environment, *args, **kwargs):
		#query for products
		products = {'products':productService.getAll()}
		template = jinja_environment.get_template('templates/products/product-list.html')
		return template.render(products)
		
def newProduct(request,jinja_environment, *args, **kwargs):
		template = jinja_environment.get_template('templates/products/new-product.html')
		return template.render()
		
def submitProduct(request,jinja_environment, *args, **kwargs):
		#code to submit
		productService.add(request.POST)
		return webapp2.redirect('/products/all')
		
def resultList(request,jinja_environment, *args, **kwargs):
		#query for products
		products = {'products':productService.getProductWithSku(request.route_kwargs['sku'])}
		template = jinja_environment.get_template('templates/products/product-list.html')
		return template.render(products)
		
def detailViewByKey(request,jinja_environment, *args, **kwargs):
		#query for products
		products = {'product':productService.getProductWithKey(request.route_kwargs['key'])}
		template = jinja_environment.get_template('templates/products/product-detail-view.html')
		return template.render(products)