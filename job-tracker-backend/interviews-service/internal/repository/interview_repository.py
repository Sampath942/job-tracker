from internal.models.interviews import Interview
from sqlmodel import Session


def create_interview(session: Session, interview_data: dict) -> Interview:
    new_interview = Interview(**interview_data)
    session.add(new_interview)
    session.flush()  
    return new_interview