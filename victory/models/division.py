from pydantic import PositiveInt
from pydantic.fields import Field

from victory.enums import ReportFormatEnum
from victory.models.base import BaseModel

__all__ = [
    "Division",
    "CreateDivisionCommand",
    "CreateDivisionReportCommand",
]


class DivisionFields:
    id = Field(description="Division id.", example=2)
    name = Field(description="Division name", example="grocery")
    format = Field(description="Report file format", example=ReportFormatEnum.CSV.value)


class BaseDivision(BaseModel):
    """Base model for division."""


class Division(BaseModel):
    id: PositiveInt = DivisionFields.id
    name: str = DivisionFields.name


# Commands.
class CreateDivisionCommand(BaseDivision):
    name: str = DivisionFields.name


class CreateDivisionReportCommand(BaseDivision):
    format: ReportFormatEnum = DivisionFields.format
