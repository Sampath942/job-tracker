
from collections.abc import Generator

from sqlmodel import Session, create_engine

from internal.config.config import settings


engine = create_engine(
    settings.postgresql_connection_string,
    pool_pre_ping=True,
)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
