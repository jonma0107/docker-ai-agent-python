from fastapi import FastAPI

fastapi_app = FastAPI()

@fastapi_app.get("/")
def read_index():
    return {"message": "Hello, world!"}

