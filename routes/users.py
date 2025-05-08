from config.api_config import app
from pydantic import BaseModel

class UsersRequestDto(BaseModel):
    email: str
    password: str
    name: str

@app.post("/users")
async def root():
    return

@app.get("/users")
async def root():
    return

@app.get("/users/{id}")
async def root():
    return

@app.patch("/users/{id}")
async def root():
    return

@app.delete("/users/{id}")
async def root():
    return