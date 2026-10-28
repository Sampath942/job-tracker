from sqlmodel import Field, SQLModel

class InterviewRoleType(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    interview_id: int = Field(foreign_key="interview.id", index=True, ondelete="CASCADE")
    roletype_id: int = Field(foreign_key="roletype.id", index=True)
