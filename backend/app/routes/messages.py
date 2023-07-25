from fastapi import APIRouter, Depends, status, Request

from app.database.dependencies import get_msg_crud
from app.database.repositories import MsgCRUD
from app.schemas import MsgBaseModel

router = APIRouter()


msg_crud = Depends(get_msg_crud)


@router.get(
    "",
    name="messages:get-all-messages",
    status_code=status.HTTP_200_OK,
)
async def get_messages(
    sender_id: int,
    recipient_id: int,
    msg_crud: MsgCRUD = msg_crud,
):
    """
    Маршрут для получения сообщений между 2 пользователями.
    :param sender_id int: id отправителя
    :param recipient_id int: id получателя
    :param msg_crud: CRUD операции для пользователя
    :return: Ответ с результатом выполнения операции
    """
    if sender_id == recipient_id:
        return {
            "message": "Echo is forbidden"
        }
    messages = await msg_crud.get_all(sender_id, recipient_id)
    if not messages:
        return {
            "message": "Messages not found"
        }
    return messages


@router.post(
    "",
    name="messages:add-message",
    status_code=status.HTTP_200_OK,
)
async def add_message(
    new_msg: MsgBaseModel,
    msg_crud: MsgCRUD = msg_crud,
):
    """
    Функция добавления пользователя
    :param new_user: UserCreate - модель создания пользователя
    :param user_crud: CRUD операции для пользователя
    :return: Ответ с результатом выполнения операции
    """
    msg_created = await msg_crud.add_msg(new_msg)
    return msg_created
