from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_async_session
from app.database.repositories import UserCRUD
from app.database.repositories import MsgCRUD


def get_user_crud(session: AsyncSession = Depends(get_async_session)) -> UserCRUD:
    return UserCRUD(session=session)


def get_msg_crud(session: AsyncSession = Depends(get_async_session)) -> MsgCRUD:
    return MsgCRUD(session=session)
