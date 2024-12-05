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

def login(usernamein):
    usernamecheck = session.query(House).filter(House.username == usernamein).first()
    if usernamecheck:
        return usernamecheck.house_id
    else:
        return -1

def houseingre(houseid):
    house_ingredients = session.query(Ingredients.ingredient_id, Ingredients.ingredient_name).join(houseIngredients, houseIngredients.ingredient_id == Ingredients.ingredient_id).filter(houseIngredients.house_id == int(houseid)).all()
    if not house_ingredients:
        return -1
    else:
        ingredient_list = []
        for ingredient in house_ingredients:
            ingredient_dict = {"id": ingredient.ingredient_id, "name": ingredient.ingredient_name}
            ingredient_list.append(ingredient_dict)
        return ingredient_list

def houserecipes(ingredientList):
    validrecipes = []
    recipelist = session.query(recipes).all()

    for currentRecipe in recipelist:
        temp = session.query(Ingredients.ingredient_name).join(recipeIngredients, recipeIngredients.ingredient_id == Ingredients.ingredient_id).filter(recipeIngredients.recipe_id == currentRecipe.recipe_id).all()
        recipe_ingredients = []
        for ingredient in temp:
            recipe_ingredients.append(ingredient[0])

        if all(ingredient in ingredientList for ingredient in recipe_ingredients):
            validrecipes.append((currentRecipe, recipe_ingredients))
    
    retRecipes = []
    if validrecipes:
        for recipe in validrecipes:
            retRecipes.append({"id": recipe[0].recipe_id,
                              "name": recipe[0].recipe_name,
                              "time": recipe[0].recipe_cooking_time,
                              "ingredients": recipe[1],
                              "link": recipe[0].recipe_link
                              })
        return retRecipes
    else:
        return {"id": -1, "name": "no recipes found"}
    

def query(username):
    houseID = login(username)
    if houseID == -1:
        return {"id": -2, "name": "input correct username"}
    else:
        ingredientsHouse = []
        for ingredient in houseingre(houseID):
            ingredientsHouse.append(ingredient["name"])
        if not ingredientsHouse:
            return {"id": -3, "name": "No ingredients found"}
        else:
            return houserecipes(ingredientsHouse)

"""value = input("username: ")
print(query(value))"""
        
session.close()
