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

    def __init__(self, date_accessed, page_accessed):
        self.date_accessed = date_accessed
        self.page_accessed = page_accessed

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def to_json(self):
        to_serialize = ['id', 'date_accessed', 'page_accessed']
        d = {}
        for attr_name in to_serialize:
            d[attr_name] = getattr(self, attr_name)
        return d

