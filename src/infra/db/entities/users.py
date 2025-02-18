from src.infra.db.config.base_entity.base import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime, timezone

class Users(Base):

    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f'Users ( username: {self.username}, created_at: {self.created_at} )'