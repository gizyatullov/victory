from pydantic import PositiveInt
from pydantic.fields import Field

from victory.enums import MeasureUnitEnum, ReportFormatEnum
from victory.models.base import BaseModel

__all__ = [
    "Assortment",
    "CreateAssortmentCommand",
    "CreateAssortmentReportCommand",
]


class AssortmentFields:
    id = Field(description="Assortment id.", example=2)
    name = Field(description="Assortment name", example="soda")
    measureunit = Field(
        description="Assortment measure unit", example=MeasureUnitEnum.THEM.value
    )
    format = Field(description="Report file format", example=ReportFormatEnum.CSV.value)


class BaseAssortment(BaseModel):
    """Base model for assortment."""


class Assortment(BaseAssortment):
    id: PositiveInt = AssortmentFields.id
    name: str = AssortmentFields.name
    measureunit: MeasureUnitEnum = AssortmentFields.measureunit


# Commands.
class CreateAssortmentCommand(BaseAssortment):
    name: str = AssortmentFields.name
    measureunit: MeasureUnitEnum = AssortmentFields.measureunit


class CreateAssortmentReportCommand(BaseAssortment):
    format: ReportFormatEnum = AssortmentFields.format
