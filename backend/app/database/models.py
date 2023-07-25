from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    """
    Модель, описывающая пользователя
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, index=True)
    user_pwd = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    user_email = Column(String, nullable=True)
    user_phone = Column(String, nullable=True)
    user_avatar = Column(String, nullable=True)


class Message(Base):
    """
    Модель, описывающая сообщение
    """
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    msg_content = Column(Text, nullable=False)
    msg_timestamp = Column(DateTime)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))
    sender = relationship("User", foreign_keys="Message.sender_id")
    recipient = relationship("User", foreign_keys="Message.recipient_id")

