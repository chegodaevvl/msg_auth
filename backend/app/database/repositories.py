from datetime import datetime
import hashlib

from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database.models import User, Message


class UserCRUD:
    """
    Реализация CRUD операций для объекта User
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self, user_name: str) -> list:
        """
        Метод получения пользователя по значению API_Key
        :return: None или объект пользователь
        """
        if not user_name:
            select_stm = select(User)
        else:
            select_stm = select(User).where(User.user_name.like(f"%{user_name}%"))
        result = await self.session.execute(select_stm)
        users = result.scalars().all()
        return users

    async def get_by_id(self, id: int) -> User:
        """
        Метод получения пользщователя по id
        :param id: int - id пользователя
        :return: None или объект пользователь
        """
        select_stm = select(User).where(User.id == id)
        query_result = await self.session.execute(select_stm)
        user = query_result.scalars().first()
        return user

    async def add_user(self, user_data) -> User:
        input_data = user_data.dict()
        new_user = User(**input_data)
        new_user.user_pwd = hashlib.sha1(bytes(new_user.user_pwd, 'utf-8')).hexdigest()
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def update_user(self, id: int, user_data) -> User:
        user = await self.get_by_id(id)
        for var, value in vars(user_data).items():
            setattr(user, var, value) if value else None

        self.session.add(user)
        await self.session.commit()
        return user

    async def delete_user(self, id: int) -> None:
        delete_stm = delete(User).where(User.id == id)
        await self.session.execute(delete_stm)
        await self.session.commit()

    async def user_exists(self, user_name):
        select_stm = select(User).where(User.user_name == user_name)
        query_result = await self.session.execute(select_stm)
        user = query_result.scalars().first()
        if not user:
            return False
        return True

    async def check_user(self, user_data):
        user_pwd = hashlib.sha1(bytes(user_data.user_pwd, 'utf-8')).hexdigest()
        select_stm = select(User).where((User.user_name == user_data.user_name) & (User.user_pwd == user_pwd))
        query_result = await self.session.execute(select_stm)
        user = query_result.scalars().first()
        if not user:
            return False
        return True


class MsgCRUD:
    """
    Реализация CRUD операций для объекта Message
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self, sender_id, recipient_id) -> list:
        """
        Метод получения пользователя по значению API_Key
        :return: None или объект пользователь
        """
        select_stm = select(Message).where((Message.sender_id == sender_id) & (Message.recipient_id == recipient_id))
        result = await self.session.execute(select_stm)
        msgs = result.scalars().all()
        return msgs

    async def msg(self, msg_data) -> Message:
        input_data = msg_data.dict()
        new_msg = Message(**input_data)
        new_msg.msg_timestamp = datetime.now()
        self.session.add(new_msg)
        await self.session.commit()
        return new_msg
