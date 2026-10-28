from sqlmodel import Field, SQLModel

class InterviewCompany(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    interview_id: int = Field(foreign_key="interview.id", index=True)
    company_id: int = Field(foreign_key="company.id", index=True)
