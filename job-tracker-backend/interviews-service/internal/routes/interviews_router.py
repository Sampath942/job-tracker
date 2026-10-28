from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from internal.services.add_interview_details import add_interview_details_service
from internal.database.databases import get_session
from internal.schemas.interview_create import InterviewCreate, InterviewRead

router = APIRouter(prefix="/api/v1/interviews", tags=["interviews"])

@router.get("/")
def get_interview_details():
    return {"message": "Interview details retrieved successfully"}

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def add_interview_details(interview_create: InterviewCreate, session: Session = Depends(get_session)) -> InterviewRead:
    return add_interview_details_service(interview_create, session)

@router.patch("/{interview_id}")
def update_interview_details(item_id: int, q: str | None = None):
    return {"message": "Interview details updated successfully"}

@router.delete("/{interview_id}")
def delete_intervew_details(item_id: int, q: str | None = None):
    return {"message": "Interview details deleted successfully"}

