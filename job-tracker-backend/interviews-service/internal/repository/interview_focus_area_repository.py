from sqlmodel import Session
from internal.models.interview_focusarea import InterviewFocusArea

def create_interview_focus_area(session: Session, interview_id: int, focus_area_id: int) -> None:
    new_interview_focus_area = InterviewFocusArea(interview_id=interview_id, focusarea_id=focus_area_id)
    session.add(new_interview_focus_area)
    session.flush()