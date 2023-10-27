from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth_bearer import JWTBearer, JWTHeader
from models.db_session import get_session
from api.descriptions.state import *
from pydantic_models.state import *
from models.state import State
from pydantic_models.state import State as StateModel

router = APIRouter()

@router.get("/get/{order_id}", summary="get state by order_id", operation_id="get-state-by-order-id",
            description=get_state_by_order_id, response_model=StateModel)
async def get_state_by_order_id(order_id: int, session: AsyncSession = Depends(get_session)):
    if state := await State.get_state_by_order_id(order_id, session):
        return StateModel.model_validate(state)
    return Response(status_code=404)

@router.get("/get/{serial_number}", summary="get state by serial number", operation_id="get-state-by-serial_number",
            description=get_state_by_serial_number, response_model=StateModel)
async def get_state_by_order_id(serial_number: str, session: AsyncSession = Depends(get_session)):
    if state := await State.get_state_by_serial_number(serial_number, session):
        return StateModel.model_validate(state)
    return Response(status_code=404)