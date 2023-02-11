import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_hello_world_text():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
