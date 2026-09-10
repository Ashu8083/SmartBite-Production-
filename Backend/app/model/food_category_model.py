from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class FoodCategory(Base):
    __tablename__ = "food_category"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        String(220),
        nullable=True
    )
    # parent_id: Mapped[int | None] = mapped_column(
    #     ForeignKey("food_category.id"),
    #     nullable=True,
    #     index=True
    # )
    #
    # # Parent category
    # parent = relationship(
    #     "FoodCategory",
    #     remote_side=[id],
    #     back_populates="children"
    # )
    #
    # # Child categories
    # children = relationship(
    #     "FoodCategory",
    #     back_populates="parent"
    # )
    package_foods = relationship(
        "PackageFood",
        back_populates="category"
    )