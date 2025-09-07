from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db, Base, engine
from app.controllers import user_controller
from app.schemas.user import UserCreate, UserResponse

# Create tables
Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db)
