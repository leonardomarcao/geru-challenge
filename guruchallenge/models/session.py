from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class Session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    date_accessed = Column(DateTime)
    page_accessed = Column(Text)

