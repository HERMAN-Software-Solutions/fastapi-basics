from fastapi import FastAPI

#create the app instance
app = FastAPI()

# Endpoint 1: The Home Page
@app.get("/")
def read_root():
    return {"message": "Welcome to my first Web API!"}

# End point 2: A dynamic URL
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}! Welcome to the server."}

# Endpoint 3: Returning a list
@app.get("/courses")
def get_courses():
    return {"courses": ["Python", "FastAPI", "Data Science"]}