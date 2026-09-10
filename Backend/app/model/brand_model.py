from sqlalchemy import Integer, String
from sympy.physics.units import au
from sqlalchemy.orm import Mapped,mapped_column

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
    
    description : Mapped[str] = mapped_column(
        String(220),nullable=True
    )
    
    country_name :Mapped[str] = mapped_column(
        String(220),nullable=True
    )    

