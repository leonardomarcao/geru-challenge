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
    session_id = Column(Text)
    date_access = Column(DateTime)


Index('session_id_idx', Session.session_id, unique=True, mysql_length=255)
