import os
import pytest

from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine

from main import app
from internal.database.databases import get_session  

TEST_DATABASE_URL = os.getenv("DATABASE_URL")

assert TEST_DATABASE_URL is not None

test_engine = create_engine(TEST_DATABASE_URL)


def override_get_session():
    with Session(test_engine) as session:
        yield session

@pytest.fixture(scope="session")
def get_test_engine():
    return test_engine

@pytest.fixture(autouse=True)
def clean_test_database():
    def clear_tables():
        # Delete child tables before parent tables.
        with test_engine.begin() as connection:
            for table in reversed(SQLModel.metadata.sorted_tables):
                connection.execute(table.delete())

    # Clean up data left by previous runs.
    clear_tables()

    yield

    # Clean up data created by this test.
    clear_tables()

@pytest.fixture
def client():
    app.dependency_overrides[get_session] = override_get_session

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_session, None)