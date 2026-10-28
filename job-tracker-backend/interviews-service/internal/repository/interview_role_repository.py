from sqlmodel import Session
from internal.models.interview_role import InterviewRole

def create_interview_role(session: Session, interview_id: int, role_id: int) -> None:
    new_interview_role = InterviewRole(interview_id=interview_id, role_id=role_id)
    session.add(new_interview_role)
    session.flush()