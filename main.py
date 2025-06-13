from fastapi import FastAPI

app = FastAPI()  # app object


@app.get("/")  # Decorator
def hello():
    return {'message': 'Hello World'}


@app.get("/about")
def about():
    return {'message': 'This is turning out to be fun'}
