from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class PackageFoodAllergen(Base):
    __tablename__ = "package_food_allergen"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    package_food_id: Mapped[int] = mapped_column(
        ForeignKey("package_food.id"),
        nullable=False,
        index=True
    )

    allergen_id: Mapped[int] = mapped_column(
        ForeignKey("allergen.id"),
        nullable=False,
        index=True
    )

    package_food = relationship(
        "PackageFood",
        back_populates="package_food_allergens"
    )

    allergen = relationship(
        "Allergen",
        back_populates="package_food_allergens"
    )