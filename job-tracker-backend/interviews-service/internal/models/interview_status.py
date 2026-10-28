from sqlmodel import Field, SQLModel

class InterviewStatus(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    interview_id: int = Field(foreign_key="interview.id", index=True)
    status_id: int = Field(foreign_key="status.id", index=True)
