from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import mapped_column, Mapped, registry 

table_registry = registry()


@table_registry.mapped_as_dataclass
class Property:
    __tablename__ = 'properties'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    description: Mapped[str]
    number_bedrroms = Mapped[str]
    price = Mapped[float]
    area = Mapped[float]
    location = Mapped[str]
    created_at = Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), nullable=True
    )