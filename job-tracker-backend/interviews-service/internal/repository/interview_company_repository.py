from sqlmodel import Session
from internal.models.interview_company import InterviewCompany

def create_interview_company(session: Session, interview_id: int, company_id: int) -> None:

    new_interview_company = InterviewCompany(interview_id=interview_id, company_id=company_id)
    session.add(new_interview_company)
    session.flush()