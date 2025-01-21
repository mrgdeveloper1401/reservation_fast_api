from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from src.postgres_alchemy import base


class DbPublicNotification(base):
    __tablename__ = "public_notification"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(Text)
    is_public = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
