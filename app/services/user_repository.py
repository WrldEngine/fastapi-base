from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository:
    def __init__(self, session: AsyncSession):
        self._session_factory = session