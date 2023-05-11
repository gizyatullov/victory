from typing import Any

from fastapi import APIRouter, BackgroundTasks, Security, status

from victory import models
from victory.db.repository.assortment import AssortmentRepository
from victory.services.report import ReportService
from victory.web.auth import access_security

router = APIRouter(dependencies=[Security(access_security)])


@router.post(
    "/",
    response_model=models.Assortment,
    status_code=status.HTTP_201_CREATED,
    summary="Create assortment",
)
async def create_assortment(
    cmd: models.CreateAssortmentCommand,
) -> Any:
    return await AssortmentRepository.create(cmd=cmd)


@router.post(
    "/report", status_code=status.HTTP_202_ACCEPTED, summary="Create assortment report"
)
async def create_assortment_report(
    cmd: models.CreateAssortmentReportCommand,
    background_tasks: BackgroundTasks,
) -> Any:
    background_tasks.add_task(ReportService.get_report_assortment, cmd=cmd)
