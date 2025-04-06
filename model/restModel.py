# Define Pydantic model for input data validation

# Import
from pydantic import BaseModel, Field, PositiveFloat


# Basig model, change for each application
class Item(BaseModel):
	name: str
	description: str | None = None
	price: float 
	price2: PositiveFloat
	tax: float | None = None
