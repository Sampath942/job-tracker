from sqlmodel import Field, SQLModel


class FocusArea(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique = True, nullable = False)
