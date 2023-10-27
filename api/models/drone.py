from sqlalchemy import Column, Integer, Numeric, String, ARRAY, select, delete
from sqlalchemy.orm import relationship
from models.db_session import SqlAlchemyBase as Base
from sqlalchemy.ext.asyncio import AsyncSession
from models.state import State


class Drones(Base):
    __tablename__ = "drones"
    serial_number = Column(String, primary_key=True)
    max_weight = Column(Numeric(4, 2), nullable=False)
    dimensions = Column(ARRAY(Integer), nullable=False)
    product_dimensions = Column(ARRAY(Integer), nullable=False)
    max_distance = Column(Integer, nullable=False)

    @classmethod
    async def get_drone(cls, drone_serial_number: str, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.serial_number == drone_serial_number))
        return _.scalar()

    @classmethod
    async def delete_drone(cls, drone_serial_number: str, admin_id: int, session: AsyncSession):
        if state := await State.get_state_by_serial_number(drone_serial_number, session):
            if state.scalar().state != "in delivery":
                await session.execute(delete(cls).where(cls.serial_number==drone_serial_number))
                return True
        return False
    
    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()