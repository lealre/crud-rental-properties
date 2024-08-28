from datetime import datetime
from enum import Enum

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


class NumBedrooms(str, Enum):
    t0 = 'T0'
    t1 = 'T1'
    t2 = 'T2'
    t3 = 'T3'
    t4 = 'T4'
    t5 = 'T5'
    t6 = 'T6'
    t6_plus = 'T6+'


@table_registry.mapped_as_dataclass
class Property:
    __tablename__ = 'properties'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    description: Mapped[str]
    number_bedrooms: Mapped[NumBedrooms]
    price: Mapped[float]
    area: Mapped[float]
    location: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
