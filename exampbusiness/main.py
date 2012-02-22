import jinja2
import os
from controllers import *
import micro_webapp2
import ajax_controller

app = micro_webapp2.WSGIApplication()
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def routeit(url,func):
        @app.route(url)
        def anonfunc(request, *args, **kwargs):
                return func(request,jinja_environment, args, kwargs)

routeit('/',main_page_controller.mainPageHandler)

routeit('/servimage/<key:\w+-\w+>',dynamic_image_controller.getImage)

routeit('/ajax',ajax_controller.testRequest)
routeit('/ajax2',ajax_controller.testRequest2)

routeit('/products/all',product_controller.listProducts)
routeit('/products/new',product_controller.newProduct)
routeit('/products/submit',product_controller.submitProduct)
routeit('/products/search/<sku:\w+>',product_controller.resultList)
routeit('/products/bykey/<key:\w+-\w+>',product_controller.detailViewByKey)


def main():
    app.run()

if __name__ == '__main__':
    main()