from typing import Union

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.services.sqlalchemy_repository import SqlAlchemyRepository
from app.models.user import User

router = APIRouter()

@router.get("/")
async def read_root():
    return {"status": "ok"}
