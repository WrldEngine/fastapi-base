from app.core.database import Base

from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)