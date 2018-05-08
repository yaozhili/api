from flask_restplus import Api

myapi = Api(
	title='OrderEase',
	version='0.1',
	catch_all_404s=True,
	serve_challenge_on_401=True
)

from order import api
myapi.add_namespace(order.api, path='api/order')
