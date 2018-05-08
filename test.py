from requests import put, get, post

res = put('http://localhost:5000/api/order', data={
  "id": 3910,
  "name": "毛血旺",
  "category": "荤菜",
  "price": 28.5,
  "stock": 99,
  "avaliable": true,
  "likes": 4,
  "description": "Hello 毛血旺"
}).json

print(res)

res = get('http://localhost:5000/api/order', data={
  "dishId": 3910
}).json

print(res)

res = post('http://localhost:5000/api/order', data={
  "id": 3910,
  "name": "毛血旺",
  "category": "荤菜",
  "price": 28.5,
  "stock": 99,
  "avaliable": true,
  "likes": 4,
  "description": "Hello 毛血旺"
}).json

print(res)