from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def welcome():
    return {"message":"Welcome to GoGiver App"}


@app.get("/api/users")
async def get_users():
    return "all users"


@app.post("/api/users")
async def create_user():
    return "all user"

@app.get("/api/users/{id}")
async def get_user():
    return "single user"


@app.put("/api/users/{id}")
async def update_user():
    return "updating user"


@app.delete("/api/users/{id}")
async def get_users():
    return "delete user"


