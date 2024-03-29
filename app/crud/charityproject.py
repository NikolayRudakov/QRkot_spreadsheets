# app/crud/charity_project.py
from typing import Optional, List

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(CharityProject.name == project_name)
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ) -> List[dict]:
        statement = (
            select(
                [
                    CharityProject.name,
                    (
                        func.julianday(
                            CharityProject.close_date
                        ) - func.julianday(CharityProject.create_date)
                    ).label("collect_time"),
                    CharityProject.description,
                ]
            )
            .where(CharityProject.fully_invested == 1)
            .order_by("collect_time")
        )

        projects = await session.execute(statement)
        projects = projects.all()
        print(projects)
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)
