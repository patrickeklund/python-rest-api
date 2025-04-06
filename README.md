# python-rest-api
python rest api


## Install dependencies

First, you need to install FastAPI and Uvicorn (the ASGI server to run your app).
```console
pip install fastapi uvicorn pydantic
```

## Run the app
To run the app use Uvicorn:

```console
uvicorn main:app --reload
```

## Testing the Endpoints

__Explanation:__
Pydantic model (Item): This model is used to validate incoming JSON data. It defines the structure and types expected in the payload (e.g., name is a string, price is a float).
- For more information about models see [pydantic](https://docs.pydantic.dev/2.3/usage/types/types/)

__FastAPI app (app):__
- The POST /items/ endpoint receives an Item object in the request body and validates it automatically.
- The GET /items/ endpoint returns a list of Item objects.
- The GET /items/{item_id} endpoint fetches a specific Item based on the item_id.


### Create an Item (POST request)
To test the POST /items/ endpoint, you can use tools like curl or Postman. Here's an example using curl:

```console
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "New Item",
  "description": "This is a new item",
  "price": 25.5,
  "price2": 25.5,
  "tax": 2.5
}'
```

### Get Items
To test the GET /items/ endpoint, you can use tools like curl or Postman. Here's an example using curl:
```console
curl -X 'GET' 'http://127.0.0.1:8000/items/'
```

### Get Item by ID
To test the GET /items/ endpoint, you can use tools like curl or Postman. Here's an example using curl:
```console
curl -X 'GET' 'http://127.0.0.1:8000/items/1'
```