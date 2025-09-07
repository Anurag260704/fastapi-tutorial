from fastapi import FastAPI
from app.routes import user_routes

app = FastAPI(title="FastAPI Node.js-Style Project")

# Register routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Hello World from FastAPI 🚀"}
