#import statements
from fastapi import APIRouter
from models.product import Product
from config.database import connection
from schemas.product import ProductEntity, ListofProductsEntity
from bson import ObjectId

ProductRouter = APIRouter()

# Get all products
@ProductRouter.get('/Products')
async def fin_all_products():
    #Once List of Product Entity is defined, connect with DB
    return ListofProductsEntity(connection.local.Product.find())

# Create  product
@ProductRouter.post('/Products')
async def create_product(product: Product):
    connection.local.Product.insert_one(dict(product))
    return ListofProductsEntity(connection.local.product.find())

#Update product
@ProductRouter.put('/Products/{sku}')
async def update_product(sku, product: Product):
    #find specific student to update
    connection.local.Product.find_update(
        {"sku": ObjectId(sku)},
        {"$set": dict(product)}
    )
    return ProductEntity(connection.local.Product.find_product({"sku": ObjectId(sku)}))

#Delete product
@ProductRouter.delete('/Products/{sku}')
async def delete_product(sku):
    #finds the product deletes and return the product object
    return ProductEntity(connection.local.Product.find_delete({"sku": ObjectId(sku)}))
