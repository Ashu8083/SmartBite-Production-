from sqlalchemy import String, Float, DateTime,Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.core.database import Base

class PackageFood(Base):
    __tablename__ = "package_food"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        String(225),
        nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
    barcode: Mapped[int] = mapped_column(
        Integer,
        nullable = True
    )
