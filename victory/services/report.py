import csv
import time
from typing import List, Type

import loguru
from pydantic import BaseModel

from victory import models
from victory.db.repository.assortment import AssortmentRepository
from victory.db.repository.devision import DivisionRepository
from victory.enums.report import ReportFormatEnum
from victory.models.exceptions.repository import EmptyResult
from victory.settings import settings

__all__ = ["ReportService"]


class ReportService:
    assortment_repository: Type[AssortmentRepository] = AssortmentRepository
    division_repository: Type[DivisionRepository] = DivisionRepository

    @classmethod
    async def write_csv(cls, data: List[BaseModel], name_prefix: str = ""):
        path = f"{settings.PATH_REPORT_SAVE}/{name_prefix}{time.time()}.csv"
        with open(path, "w", newline="") as csvfile:
            fieldnames = list(data[0].dict().keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            data = [item.dict() for item in data]
            writer.writerows(data)

    @classmethod
    async def get_report_division(cls, cmd: models.CreateDivisionReportCommand):
        try:
            data = await cls.division_repository.read_all()
        except EmptyResult:
            loguru.logger.info("No data in division table")
            return
        if cmd.format == ReportFormatEnum.CSV:
            await cls.write_csv(data=data, name_prefix="division")

    @classmethod
    async def get_report_assortment(cls, cmd: models.CreateAssortmentReportCommand):
        try:
            data = await cls.assortment_repository.read_all()
        except EmptyResult:
            loguru.logger.info("No data in assortment table")
            return
        if cmd.format == ReportFormatEnum.CSV:
            await cls.write_csv(data=data, name_prefix="assortment")
