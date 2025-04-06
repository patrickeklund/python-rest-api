# Import
from fastapi import FastAPI, HTTPException
from typing import List
# - Code
from model.restModel import Item
from helpers.helpers import runShellScript


# Create FastAPI app instance
app = FastAPI()

# Endpoint to create an item (POST request)
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
	# Example: Add custom business logic, such as validation or processing
	if item.price < 0:
		raise HTTPException(status_code=400, detail="Price must be greater than zero")

	# Bash script
	runShellScript("my_script.sh")

	return item

# Endpoint to get list of items (GET request)
@app.get("/items/", response_model=List[Item])
async def get_items():
	# Example: In a real app, fetch from a database
	sample_items = [
		Item(name="Item 1", description="A description", price=20.0, tax=2.0),
		Item(name="Item 2", description="Another description", price=30.0, tax=3.0)
	]
	return sample_items

# Endpoint to get an item by ID (GET request)
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
	# In a real app, fetch data based on the item_id (e.g., from a database)
	if item_id == 1:
		return Item(name="Item 1", description="A description", price=20.0, tax=2.0)
	elif item_id == 2:
		return Item(name="Item 2", description="Another description", price=30.0, tax=3.0)
	else:
		raise HTTPException(status_code=404, detail="Item not found")