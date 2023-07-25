from fastapi import APIRouter, Depends, status, Request

from app.database.dependencies import get_user_crud
from app.database.repositories import UserCRUD
from app.schemas import UserCreate, UserCreated, UserUpdate

router = APIRouter()


user_crud = Depends(get_user_crud)


@router.get(
    "",
    name="users:get-all-users",
    status_code=status.HTTP_200_OK,
)
async def get_all_users(
    user_name: str = None,
    user_crud: UserCRUD = user_crud,
):
    """
    Маршрут для получения данных о пользователях, с возможностью поиска по части user_name.
    :param user_name: str, часть имени пользователя для поиска. По умолчанию пусто.
    :param user_crud: CRUD операции для пользователя
    :return: Ответ с результатом выполнения операции
    """
    users = await user_crud.get_all(user_name)
    if not users:
        return {
            "message": "Users not found"
        }
    return users


@router.post(
    "",
    name="users:add-user",
    status_code=status.HTTP_200_OK,
)
async def add_user(
    new_user: UserCreate,
    user_crud: UserCRUD = user_crud,
):
    """
    Функция добавления пользователя
    :param new_user: UserCreate - модель создания пользователя
    :param user_crud: CRUD операции для пользователя
    :return: Ответ с результатом выполнения операции
    """
    print(new_user.user_name)
    if await user_crud.user_exists(new_user.user_name):
        return {
            "message": "User already exist"
        }
    user_created = await user_crud.add_user(new_user)
    return user_created


@router.get(
    "/{id}",
    name="users:get-user-by-id",
    status_code=status.HTTP_200_OK,
)
async def get_user_by_id(
    id: int,
    user_crud: UserCRUD = user_crud,
):
    """
    Маршрут для получения информации о пользователе по id
    :param id: int - id пользователя
    :param user_crud: CRUD операции для пользователя
    :return: Ответ с результатом выполнения операции (информация о пользователе,
             информация об ошибке)
    """
    user = await user_crud.get_by_id(id)
    if not user:
        return {
            "message": "User not found"
        }
    return user


@router.put(
    "/{id}",
    name="users:update-user-info",
    status_code=status.HTTP_200_OK,
)
async def update_user(
    id: int,
    user_data: UserUpdate,
    user_crud: UserCRUD = user_crud,
):
    """
    Маршрут для получения информации о пользователе по id
    :param id: int - id пользователя
    :param api_key: str - api_key для доступа к api
    :param user_crud: CRUD операции для пользователя
    :return: Ответ с результатом выполнения операции (информация о пользователе,
             информация об ошибке)
    """
    user = await user_crud.get_by_id(id)
    if not user:
        return {
            "message": "User not found"
        }
    user = await user_crud.update_user(id, user_data)
    return user


@router.delete(
    "/{id}",
    name="users:delete-user",
    status_code=status.HTTP_200_OK,
)
async def delete_user(
    id: int,
    user_crud: UserCRUD = user_crud,
):
    """
    Функция удаления пользователя по его id
    :param id: int - id пользователя
    :param user_crud: CRUD операции для пользователя
    :return: Ответ с результатом выполнения операции
    """
    user = await user_crud.get_by_id(id)
    if not user:
        return {
            "message": "User not found"
        }
    await user_crud.delete_user(id)
    return {
        "message": "User deleted"
    }
