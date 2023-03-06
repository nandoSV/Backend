# Backend instructions
## Fernando Romero

1. Install python
2. Install mongodb
3. Use pycharm or Visual Studio
4. use git bash or Ubuntu
5. Git repository: _(mine is called Backend for this project.)_
6. Git clone repository and open in a source-code editor.
7. Donwload Conda and create env
8. Donwload packages inside your env
    --pip instal pymongo fastapi uvicorn--
9. Create index.py, database.py in config folder, and product.py in models, routes and schemas folders.
10. Create Database connection   
11. Use uvicorn index:app --reload 
to run the program locally and later you can check endpoints once are made by using the link:
    --http://127.0.0.1:8000/docs#/--
11. Create product model in models folder with pydantic BaseModel
12. create router in models folder using APIRouter
13. Include router in the index
14. Create product entity dictionary and the list of product entity in product.py in schemas folder. Don't forget to import statment in router




