from typing import Union

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.services.sqlalchemy_repository import SqlAlchemyRepository
from app.schemas.user_schema import UserModel
from app.models.user import User

router = APIRouter()

@router.get("/")
async def read_root() -> None:
    return {"status": "ok"}

@router.post("/set_users", response_model=UserModel)
async def set_user(user_data: UserModel, session: AsyncSession = Depends(get_session)) -> UserModel:
    
    user_repo = SqlAlchemyRepository(model=User, db_session=session)
    created_user = await user_repo.create(user_data)

    return UserModel(name=created_user.name)