from fastapi import APIRouter
from app.models.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix = "/users", tags = ["users"])

user_service = UserService()

@router.post("/", response_model = UserResponse)
def create_user(user: UserCreate):
    return user_service.create_user(user)

@router.get("/", response_model = list[UserResponse])
def list_users():
    return user_service.list_users()