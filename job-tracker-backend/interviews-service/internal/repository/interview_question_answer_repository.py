from sqlmodel import Session
from internal.models.interview_question_answer import InterviewQuestionAnswer

def create_interview_question_answer(session: Session, interview_id: int, question: str, answer: str) -> None:
    new_interview_question_answer = InterviewQuestionAnswer(interview_id=interview_id, question=question, answer=answer)
    session.add(new_interview_question_answer)
    session.flush()