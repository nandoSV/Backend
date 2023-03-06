#import statements
from fastapi import APIRouter
from models.product import Product
from config.database import connection
from schemas.product import ProductEntity, ListofProductsEntity

ProductRouter = APIRouter()

# Get all products
@ProductRouter.get('/Products')
async def fin_all_products():
    #Once List of Product Entity is defined, connect with DB
    return ListofProductsEntity(connection.local.Product.find())

# Create a product
@ProductRouter.post('/Products')
async def create_product(product: Product):
    connection.local.Product.insert_one(dict(product))
    return ListofProductsEntity(connection.local.Product.find())
