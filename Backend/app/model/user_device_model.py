from sqlalchemy import Column, DateTime, Integer, ForeignKey,UUID
import uuid
from sqlalchemy.orm import Mapped,mapped_column,relationship

from app.core.database import Base

class UserDevice(Base):
    __tablename__ = "user_device"
    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
    )
    user_id : Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )
    device_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
    )

    users = relationship("Users",
                         back_populates="device",)

