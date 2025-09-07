from app.models.user import User, UserCreate, UserResponse

class UserService:
    def __init__(self):
        self._users: list[User] = []
        self._id_counter = 1

    def create_user(self, user_data: UserCreate) -> UserResponse:
        user = User(id = self._id_counter, name=user_data.name, email=user_data.email)
        self._users.append(user)
        self._id_counter += 1
        return UserResponse(id = user.id, name = user.name, email = user.email)
    
    def list_users(self) -> list[UserResponse]:
        return [UserResponse(id = u.id, name = u.name, email = u.email) for u in self._users]
