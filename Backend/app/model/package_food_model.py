from sqlalchemy import String, Float, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.database import Base

class PackageFood(Base):
    __tablename__ = "package_food"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True
    )
    brand_id: Mapped[int] = mapped_column(
        ForeignKey("brand.id"),
        nullable=False,
        index=True
    )
    barcode: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        unique=True
    )
    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
        unique=True
    )
    price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("food_category.id"),
        nullable=True
    )
    allergens_id: Mapped[int] = mapped_column(
        ForeignKey("allergen.id"),
    )

    serving_size: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    serving_unit: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )
    quantity: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )
    quantity_unit: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )
    food_claims :Mapped[str | None] = mapped_column(
        String(225),
        nullable=True,
    )
    brand = relationship(
        "Brand",
        back_populates="package_food"
    )
    package_food_nutrient = relationship(
        "PackageFoodNutrient",
        back_populates="package_food",
        cascade="all, delete-orphan"
    )
    package_food_allergens = relationship(
        "PackageFoodAllergen",
        back_populates="package_food",
        cascade="all, delete-orphan"
    )
    category = relationship(
        "FoodCategory",
        back_populates="package_foods"
    )