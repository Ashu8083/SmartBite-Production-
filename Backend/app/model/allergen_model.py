from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy  import Integer,String
from app.core.database import Base

class Allergen(Base):
    __tablename__ = "allergen"

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

    description: Mapped[str | None] = mapped_column(
        String(220),
        nullable=True
    )

    package_food_allergens = relationship(
        "PackageFoodAllergen",
        back_populates="allergen",
        cascade="all, delete-orphan"
    )