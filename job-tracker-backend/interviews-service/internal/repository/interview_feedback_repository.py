from sqlmodel import Session
from internal.models.interview_feedback import InterviewFeedback

def create_interview_feedback(session: Session, interview_id: int, feedback: str) -> None:
    new_interview_feedback = InterviewFeedback(interview_id=interview_id, feedback=feedback)
    session.add(new_interview_feedback)
    session.flush()