from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from src.postgres_alchemy import base, engine

from .enums import Enum, RoleUser

role_user_enum = ENUM(RoleUser, name="roleuser")
role_user_enum.create(engine, checkfirst=True)

class DbUser(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    role = Column(role_user_enum, default=RoleUser.normal)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    profile = relationship("DbUserProfile", back_populates="profile", uselist=False)
    notification = relationship("DbUserPrivateNotification", back_populates="user_notification")
    user_device = relationship("DbUserDevice", back_populates="user_device")


class DbUserProfile(base):
    __tablename__ = "user_profile"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)


class DbUserPrivateNotification(base):
    __tablename__ = "user_private_notification"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    is_public = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))


class DbUserDevice(base):
    __tablename__ = "user_device"
    id = Column(Integer, primary_key=True, index=True)
    user_agent = Column(String)
    user_ip = Column(String)
    user_device_name = Column(String, nullable=True)
    user_device_os = Column(String, nullable=True)
    is_blocked = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))
