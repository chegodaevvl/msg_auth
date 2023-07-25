from fastapi import APIRouter, Depends, status, Request

from app.database.dependencies import get_user_crud
from app.database.repositories import UserCRUD
from app.schemas import UserLogin
from app.auth.auth_handler import signJWT

router = APIRouter()


user_crud = Depends(get_user_crud)


@router.post(
    "",
    name="login",
    status_code=status.HTTP_200_OK,
)
async def user_login(
    user_data: UserLogin,
    user_crud: UserCRUD = user_crud,
):
    if user_crud.check_user(user_data):
        return signJWT(user_data.user_name)
    return {
        "message": "Wrong login details!"
    }