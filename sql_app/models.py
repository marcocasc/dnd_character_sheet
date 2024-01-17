from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    sheets = relationship("Sheet", back_populates="owner")

class Sheet(Base):
    __tablename__ = "sheets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    creation_date = Column(DateTime, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))

    owner = relationship("User", back_populates="sheets")
    character = relationship("Character", back_populates="character")

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    sheet_id = Column(Integer, ForeignKey("sheets.id"))

    sheet = relationship("Sheet", back_populates="character")
