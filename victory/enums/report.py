from enum import Enum

__all__ = ["ReportFormatEnum"]


class ReportFormatEnum(str, Enum):
    CSV = "csv"
