from sqlalchemy import Column, Integer, select, Numeric, String, ForeignKey
from models.db_session import SqlAlchemyBase as Base
from sqlalchemy.ext.asyncio import AsyncSession
from models.order import Orders

class State(Base):
    __tablename__ = "state"
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, ForeignKey("drones.serial_number", ondelete="cascade"), nullable=False)
    order_id = Column(Integer, ForeignKey(Orders.id))
    state = Column(String, nullable=False)
    latitude = Column(Numeric(8, 6), nullable=False)
    longitude = Column(Numeric(8, 6), nullable=False)

    @classmethod
    async def get_state_by_serial_number(cls, serial_number: str, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.serial_number==serial_number))
        return _.scalar()

    @classmethod
    async def get_state_by_order_id(cls, order_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.order_id==order_id))
        return _.scalar()
    
    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()