import uuid
from sqlalchemy.orm import relationship,mapped_column,Mapped
from sqlalchemy import ForeignKey,UUID,Float

from app.core.database import Base

class PackageFoodNutrient(Base):
    __tablename__ = "nutrition_nutrient"
    id: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        default=uuid.uuid4,
    )
    package_id: Mapped[int] = mapped_column(
        ForeignKey("package_food.id"),
        nullable=False,
        index=True
    )
    nutrient_id: Mapped[int] = mapped_column(
        ForeignKey("nutrient.id"),
        nullable=False,
        index=True
    )
    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
    package_food = relationship(
        "PackageFood",
        back_populates=""
    )
    nutrient = relationship(
        "Nutrient")