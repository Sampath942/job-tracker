from sqlmodel import Session
from internal.models.interview_status import InterviewStatus

def create_interview_status(session: Session, interview_id: int, status_id: int) -> None:
    new_interview_status = InterviewStatus(interview_id=interview_id, status_id=status_id)
    session.add(new_interview_status)
    session.flush()