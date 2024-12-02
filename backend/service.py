from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.sql import text

Database_url = "sqlite:///ssh_database.db"

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)  
    username = Column(String)  
    password = Column(String)

class Useringredients(Base):
    __tablename__ = "user_ingredients"

    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.ingredient_id'), primary_key=True)

class Ingredients(Base):
    __tablename__ = "ingredients"

    ingredient_id = Column(Integer, primary_key=True)
    ingredient_name = Column(String)

engine = create_engine(Database_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def login():
    usernamein = input("enter username: ")
    usernamecheck = session.query(User).filter(User.username == usernamein).all()
    if usernamecheck:
        passwordin = input("enter password: ")
        passwordcheck = session.query(User).filter(User.username == usernamein, User.password == passwordin).first()
        if passwordcheck:
            print("correct username and password!")
            return passwordcheck.user_id
        else:
            print("incorrect password\n")
    else:
        print("incorrect username\n")

def useringre(userid):
    user_ingredients = session.query(Ingredients.ingredient_name).join(Useringredients, Useringredients.ingredient_id == Ingredients.ingredient_id).filter(Useringredients.user_id == int(userid)).all()
    if not user_ingredients:
        print("invalid input\n")
    else:
        for ingredient in user_ingredients:
            print(ingredient.ingredient_name)

value = login()
if value != None:
    useringre(value)

session.close()
