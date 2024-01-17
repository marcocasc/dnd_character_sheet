from pydantic import BaseModel


class SheetBase(BaseModel):
    title: str


class SheetCreate(SheetBase):
    pass


class Sheet(SheetBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    sheet: list[Sheet] = []

    class Config:
        orm_mode = True
