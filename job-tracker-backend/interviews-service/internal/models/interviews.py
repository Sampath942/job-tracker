from sqlmodel import Field, SQLModel
from datetime import date


class Interview(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    job_link: str | None = None
    date_of_interview: date = Field(index = True)
