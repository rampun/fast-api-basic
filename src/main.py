import uvicorn
from fastapi import FastAPI

app = FastAPI()

user_db = {
    'jack': {'username': 'jack', 'date_joined': '2021-12-01', 'location': 'TST'},
    'jill': {'username': 'jill', 'date_joined': '2021-12-02', 'location': 'YMT'},
    'yueng': {'username': 'yueng', 'date_joined': '2021-12-03', 'location': 'SSP'},
}


@app.get('/')
def get_hello_world_text():
    return {"result": "This is hello world text new updated"}


@app.get('/users')
def get_detail():
    user_list = list(user_db)
    return user_list


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
