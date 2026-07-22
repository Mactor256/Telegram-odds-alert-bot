from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)


class Base(DeclarativeBase):
    pass


class Pick(Base):

    __tablename__ = "picks"

    id = Column(
        Integer,
        primary_key=True
    )

    event = Column(
        String
    )

    market = Column(
        String
    )

    odds = Column(
        Float
    )

    status = Column(
        String,
        default="pending"
    )
