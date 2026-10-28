from sqlmodel import Field, SQLModel

class InterviewFocusArea(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    interview_id: int = Field(foreign_key="interview.id", index=True)
    focusarea_id: int = Field(foreign_key="focusarea.id", index=True)
