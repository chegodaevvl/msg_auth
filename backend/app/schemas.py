from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class CoreModel(BaseModel):
    pass


class IDModelMixin(BaseModel):
    """
    Миксин для добавления в модель поля id
    """
    id: int


class UserBasicModel(CoreModel):
    user_name: str


class UserUpdate(CoreModel):
    first_name: Optional[str]
    last_name: Optional[str]
    user_email: Optional[EmailStr]
    user_phone: Optional[PhoneNumber]
    user_avatar: Optional[str]


class UserCreate(UserBasicModel, UserUpdate):
    user_pwd: str


class UserDetail(IDModelMixin, UserUpdate):
    pass

    class Config:
        from_attributes = True


class UserCreated(IDModelMixin, UserBasicModel):
    pass


class UserLogin(CoreModel):
    user_name: str
    user_pwd: str


class MsgBaseModel(CoreModel):
    msg_content: str
    sender_id: int
    recipient_id: int


class MsgDetail(IDModelMixin, MsgBaseModel):
    msg_timestamp: datetime
