#import statements
from fastapi import FastAPI
from routes.product import ProductRouter

#Create App
app = FastAPI()

#include router
app.include_router(ProductRouter)