#!/usr/bin/python3
"""Class user
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User
    ""
    __tablename__ = "users"
    email = Column(String(128),nullable=False)
    password = Column(String(128),nullable=False)
    first_name = Column(String(128),nullable=True)
    last_name = Column(String(128),nullable=True)
    places = relationship("Place",backref="User",cascade="all, delete")
    reviews = relationship("Review",backref="User",cascade="all, delete")
