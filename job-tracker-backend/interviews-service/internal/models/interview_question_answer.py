from sqlmodel import Field, SQLModel

class InterviewQuestionAnswer(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    interview_id: int = Field(foreign_key="interview.id", index=True)
    question: str
    answer: str
