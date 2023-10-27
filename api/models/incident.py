from sqlalchemy import Column, Integer, String, select, ForeignKey
from models.db_session import SqlAlchemyBase as Base
from sqlalchemy.ext.asyncio import AsyncSession
from models.drone import Drones


class Incidents(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, ForeignKey(Drones.serial_number, ondelete="cascade"), nullable=False)
    text = Column(String, nullable=False)