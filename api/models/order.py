from sqlalchemy import Column, Integer, select, Numeric, ARRAY
from models.db_session import SqlAlchemyBase as Base
from sqlalchemy.ext.asyncio import AsyncSession

class Orders(Base):
    __tablename__="orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    dimensions = Column(ARRAY(Integer), nullable=False)
    weight = Column(Integer, nullable=False)
    latitude = Column(Numeric(8, 6), nullable=False)
    longitude = Column(Numeric(8, 6), nullable=False)