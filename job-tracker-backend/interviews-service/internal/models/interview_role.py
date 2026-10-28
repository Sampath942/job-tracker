from sqlmodel import Field, SQLModel

class InterviewRole(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    interview_id: int = Field(foreign_key="interview.id", index=True, ondelete="CASCADE")
    role_id: int = Field(foreign_key="role.id", index=True)
