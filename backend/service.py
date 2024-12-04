from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.sql import text

Database_url = "sqlite:///ssh_database.db"

Base = declarative_base()

class House(Base):
    __tablename__ = 'houses'
    
    house_id = Column(Integer, primary_key=True)  
    username = Column(String)  
    password = Column(String)

class houseIngredients(Base):
    __tablename__ = "house_ingredients"

    house_id = Column(Integer, ForeignKey('houses.house_id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.ingredient_id'), primary_key=True)

class Ingredients(Base):
    __tablename__ = "ingredients"

    ingredient_id = Column(Integer, primary_key=True)
    ingredient_name = Column(String)

class recipes(Base):
    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key=True)  
    recipe_name = Column(String)  
    recipe_link = Column(String)
    recipe_cooking_time = Column(Integer)

class recipeIngredients(Base):
    __tablename__ = "recipe_ingredient"

    recipe_id = Column(Integer, ForeignKey('recipes.recipe_id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.ingredient_id'), primary_key=True)

engine = create_engine(Database_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def login():
    usernamein = input("enter username: ")
    usernamecheck = session.query(House).filter(House.username == usernamein).all()
    if usernamecheck:
        passwordin = input("enter password: ")
        passwordcheck = session.query(House).filter(House.username == usernamein, House.password == passwordin).first()
        if passwordcheck:
            print("correct username and password!")
            return passwordcheck.house_id
        else:
            print("incorrect password\n")
    else:
        print("incorrect username\n")

def houseingre(houseid):
    house_ingredients = session.query(Ingredients.ingredient_name).join(houseIngredients, houseIngredients.ingredient_id == Ingredients.ingredient_id).filter(houseIngredients.house_id == int(houseid)).all()
    if not house_ingredients:
        print("No ingredients found.\n")
    else:
        ingredientnames = []
        for ingredient in house_ingredients:
            ingredientnames.append(ingredient[0])
        return ingredientnames

def houserecipes(ingredientList):
    validrecipes = []


    recipelist = session.query(recipes).all()

    for currentRecipe in recipelist:
        temp = session.query(Ingredients.ingredient_name).join(recipeIngredients, recipeIngredients.ingredient_id == Ingredients.ingredient_id).filter(recipeIngredients.recipe_id == currentRecipe.recipe_id).all()
        recipe_ingredients = []
        for ingredient in temp:
            recipe_ingredients.append(ingredient[0])

        if all(ingredient in ingredientList for ingredient in recipe_ingredients):
            validrecipes.append(currentRecipe)
      
    if validrecipes:
        for recipe in validrecipes:
            print(f"Recipe name: {recipe.recipe_name}, Recipe Link: {recipe.recipe_link}, Recipe time: {recipe.recipe_cooking_time}")
    else:
        print("No recipes found with the available ingredients.")

houseid = login()
if houseid:
    ingredientsList = houseingre(houseid)
    if ingredientsList:
        houserecipes(ingredientsList)
        
session.close()
