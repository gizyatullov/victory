from typing import Any

from fastapi import APIRouter, BackgroundTasks, Security, status

from victory import models
from victory.db.repository.devision import DivisionRepository
from victory.services.report import ReportService
from victory.web.auth import access_security

router = APIRouter(dependencies=[Security(access_security)])


@router.post(
    "/",
    response_model=models.Division,
    status_code=status.HTTP_201_CREATED,
    summary="Create division",
)
async def create_division(
    cmd: models.CreateDivisionCommand,
) -> Any:
    return await DivisionRepository.create(cmd=cmd)


@router.post(
    "/report", status_code=status.HTTP_202_ACCEPTED, summary="Create division report"
)
async def create_division_report(
    cmd: models.CreateDivisionReportCommand,
    background_tasks: BackgroundTasks,
) -> Any:
    background_tasks.add_task(ReportService.get_report_division, cmd=cmd)
