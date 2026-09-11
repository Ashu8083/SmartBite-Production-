import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Column, DateTime, Integer, ForeignKey,UUID ,String ,Boolean

from app.core.database import Base
from app.model.timestamp import TimestampMixin


class UserDevice(Base,TimestampMixin):
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
    device_type: Mapped[str] = mapped_column(String)
    firebase_fcm_token: Mapped[str] = mapped_column(String)

    last_login: Mapped[datetime] = mapped_column(DateTime)
    logout_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    is_login: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    users = relationship("Users",
                         back_populates="user_device",)

