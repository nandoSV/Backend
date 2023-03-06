#import statements
from pydantic import BaseModel

class Product(BaseModel):
    ProductName: str
    ProductSKU: str
    ProductTitle: str
    ProductDescription: str
    ProductPrice: float
