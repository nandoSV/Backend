# API schema helps developers interact with an API, 
# and the standardization of that schema has made the 
# integration process much more automated.

def ProductEntity(DBItem) -> dict:
    return {
        "SKU": str(DBItem["_ProductSKU"]),
        "Name": str(DBItem["ProductName"]),
        "Title": str(DBItem["ProductTitle"]),
        "Description": str(DBItem["ProductDescription"]),
        "Price": float(DBItem["ProductPrice"])
    }

def ListofProductsEntity(DBItemList) -> list:
    ListProducts = []
    for item in DBItemList:
        ListProducts.append(ProductEntity(item))
    return ListProducts