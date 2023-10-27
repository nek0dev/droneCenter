from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth_bearer import JWTBearer, JWTHeader
from models.db_session import get_session
from descriptions.drone import *
from pydantic_models.drone import *
from models.drone import Drones
from models.state import State

router = APIRouter()

@router.post("/create", summary="create drone", operation_id="create-drone",
             description=create_drone, response_model=Drone)
async def create_drone(new_drone: CreateDrone, session: AsyncSession = Depends(get_session), token: JWTHeader = Depends(JWTBearer())):
    drone = Drones(serial_number=new_drone.serial_number, max_weight=Decimal(float(new_drone.max_weight) * 0.9), dimensions=new_drone.dimensions, product_dimensions=new_drone.product_dimensions, max_distance=new_drone.max_distance)
    await drone.save(session)
    state = State(serial_number=drone.serial_number, state='in base', latitude=new_drone.latitude, longitude=new_drone.longitude)
    await state.save(session)
    return Drone.model_validate(drone)

@router.get("/get/{serial_number}", summary="get drone by serial number", operation_id="get-drone-by-serial-number",
            description=get_drone_by_serial_number, response_model=Drone)
async def get_drone_by_id(serial_number: str, session: AsyncSession = Depends(get_session), token: JWTHeader = Depends(JWTBearer())):
    if drone := await Drones.get_drone(serial_number, session):
        return Drone.model_validate(drone)
    return Response(status_code=404)

@router.post("/delete", summary="delete drone by serial number", operation_id="delete-drone-by-serial-number",
             description=delete_drone_by_serial_number, response_class=Response)
async def delete_drone(delete: DeleteDrone, session: AsyncSession = Depends(get_session), token: JWTHeader = Depends(JWTBearer())):
    delete_status = await Drones.delete_drone(delete.serial_number, token.admin_id, session)
    if delete_status:
        return Response(status_code=201)
    return Response(status_code=404)

@router.get('/all', summary="get all orders", operation_id="get-all-orders",
            description=get_all_drones, response_model=list[Drone])
async def get_all_drones(session: AsyncSession = Depends(get_session), token: JWTHeader = Depends(JWTBearer())):
    if drones := await Drones.get_all_drones(token.admin_id, session):
        return [
            Drone.model_validate(drone)
            for drone in drones
        ]
    return Response(status_code=404)

@router.post("/change", summary='change drone', operation_id="change-drone",
             description=change_drone, response_class=Response)
async def change_drone(change: ChangeDrone, session: AsyncSession = Depends(get_session), token: JWTHeader = Depends(JWTBearer())):
    resp = await Drones.change_drone(change.serial_number, change.max_weight, change.product_dimensions, change.max_distance, token.admin_id, session)
    if resp:
        return Response(status_code=201)
    return Response(status_code=404)