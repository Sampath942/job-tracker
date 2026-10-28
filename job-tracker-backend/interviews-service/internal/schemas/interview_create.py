from datetime import date

from sqlmodel import Field, SQLModel


class InterviewCreate(SQLModel):
    company_name: str
    role: str
    role_type: str
    status: str
    focus_areas: list[str] = Field(default_factory=list)
    job_link: str | None = None
    date_of_interview: date | None = None
    questions: list[str] = Field(default_factory=list)
    answers: list[str] = Field(default_factory=list)
    feedback: str | None = None


class InterviewRead(SQLModel):
    id: int
    