from sqlalchemy import Integer, ForeignKey, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Nutrient(Base):
    __tablename__ = "nutrient"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )
    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )