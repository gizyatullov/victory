from enum import Enum

__all__ = ["MeasureUnitEnum"]


class MeasureUnitEnum(str, Enum):
    THEM = "them"
    LITER = "liter"
