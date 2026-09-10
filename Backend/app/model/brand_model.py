from sqlalchemy import Integer, String
from sympy.physics.units import au
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model import PackageFood
from app.core.database import Base


class Brand(Base):
    __tablename__ = "brand"

    id  : Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = True,
        unique = True,
        nullable = False
    )
    name : Mapped[str]  = mapped_column(
        String(100),
    )
    logo_url : Mapped[str] = mapped_column(
        String(500),
        nullable = True
    )
    website_url : Mapped[str] = mapped_column(
        String(500),
        nullable = True
    )
    description : Mapped[str] = mapped_column(
        String(220),nullable=True
    )
    country_name :Mapped[str] = mapped_column(
        String(220),nullable=True
    )

    package_food = relationship(
        PackageFood,
        back_populates="brand",
        cascade="all, delete-orphan"
    )


