from flask_restplus import Api

myapi = Api(
	title='OrderEase',
	version='0.1',
	catch_all_404s=True,
	serve_challenge_on_401=True
)

from .order import api as order_api
myapi.add_namespace(order_api, path='api/order')
