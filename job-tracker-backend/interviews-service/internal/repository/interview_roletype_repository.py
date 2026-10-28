from sqlmodel import Session
from internal.models.interview_roletype import InterviewRoleType

def create_interview_roletype(session: Session, interview_id: int, roletype_id: int) -> None:
    new_interview_roletype = InterviewRoleType(interview_id=interview_id, roletype_id=roletype_id)
    session.add(new_interview_roletype)
    session.flush()