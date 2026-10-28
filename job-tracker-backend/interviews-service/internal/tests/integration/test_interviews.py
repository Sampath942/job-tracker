import datetime
from fastapi.testclient import TestClient
import pytest
from sqlmodel import Session, column, select
from internal.models.interviews import Interview
from internal.models.company import Company
from internal.models.interview_feedback import InterviewFeedback

import internal.services.add_interview_details as add_interview_details_service

def test_create_interview(client, get_test_engine):
    response = client.post(
        "/api/v1/interviews",
        json={
            "date_of_interview": "2026-10-21",
            "job_link": "https://example.com/jobs/123",
            "company_name": "Example Corp",
            "role": "Backend Developer",
            "role_type": "Full-time",
            "status": "Completed",
            "focus_areas": ["Go", "PostgreSQL"],
            "questions": ["Explain database indexing", "Explain an issue you fixed in production"],
            "answers": ["Indexes can accelerate lookups.", ""],
            "feedback": (
                "The interviewer asked about "
                "O'Reilly's database design."
            ),
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["id"] is not None

    with Session(get_test_engine) as session:
        interviews = session.exec(
            select(Interview)).all()

        assert len(interviews) == 1
        assert interviews[0].date_of_interview == datetime.date(2026, 10, 21)
        assert interviews[0].job_link == "https://example.com/jobs/123"

def test_create_interview_missing_company_name(client):
    payload = {
        "role": "Backend Developer",
        "role_type": "Full time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_missing_role(client):
    payload = {
        "company_name": "Google",
        "role_type": "Full time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_missing_roletype(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Engineer",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_missing_status(client):
    payload = {
        "company_name": "Google",
        "role_type": "Full time",
        "role": "Backend Engineer",
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_invalid_date_format(client):
    payload = {
            "company_name": "Google",
            "role": "Backend Developer",
            "role_type": "Full time",
            "status": "Applied",
            "date_of_interview": "21-10-2026",
        }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422


def test_create_interview_impossible_date(client):
    payload = {
                "company_name": "Google",
                "role": "Backend Developer",
                "role_type": "Full time",
                "status": "Applied",
                "date_of_interview": "2026-02-30",
            }
    

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_company_name(client):
    payload = {
        "company_name": 123,
        "role": "Backend Developer",
        "role_type": "Full time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_role(client):
    payload = {
        "company_name": "Google",
        "role": 123,
        "role_type": "Full time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_role_type(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Developer",
        "role_type": 123,
        "status": "Applied",
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_status(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Developer",
        "role_type": "Full Time",
        "status": 123,
        "date_of_interview": "2026-10-21",
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_focus_areas(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Developer",
        "role_type": "Full Time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
        "focus_areas": "System Design"
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_job_link(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Developer",
        "role_type": "Full Time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
        "job_link": 123
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_questions(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Developer",
        "role_type": "Full Time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
        "questions": "Explain your projects",
        "answers": ["Golang based project"]
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_answers(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Developer",
        "role_type": "Full Time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
        "questions": ["Explain your projects"],
        "answers": "Golang based project"
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_wrong_format_feedback(client):
    payload = {
        "company_name": "Google",
        "role": "Backend Developer",
        "role_type": "Full Time",
        "status": "Applied",
        "date_of_interview": "2026-10-21",
        "feedback": 123
    }

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 422

def test_create_interview_rolls_back_on_mid_transaction_failure(
    client, monkeypatch, get_test_engine
):
    job_link = "https://example.com/jobs/rollback-test"

    def fail_association(*args, **kwargs):
        raise RuntimeError("Simulated database failure")

    monkeypatch.setattr(
        add_interview_details_service,
        "create_interview_focus_area",
        fail_association,
    )

    payload = {
        "date_of_interview": "2026-10-21",
        "job_link": job_link,
        "company_name": "Rollback Test Company",
        "role": "Rollback Test Engineer",
        "role_type": "Full-time",
        "status": "Applied",
        "focus_areas": ["Rollback Test Focus"],
        "questions": [],
        "answers": [],
    }

    # TestClient normally re-raises unhandled application exceptions.
    with pytest.raises(RuntimeError, match="Simulated database failure"):
        client.post("/api/v1/interviews", json=payload)

    # Open a fresh session to verify what was actually committed.
    with Session(get_test_engine) as session:
        interview = session.exec(
            select(Interview).where(Interview.job_link == job_link)
        ).first()

        assert interview is None

def test_create_interview_case_sensitive(client, get_test_engine):
    response = client.post(
        "/api/v1/interviews",
        json={
            "company_name": "Google",
            "role": "Backend Developer",
            "role_type": "Full-time",
            "status": "Rejected",
            "date_of_interview": "2026-10-21",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["id"] is not None


    response = client.post(
        "/api/v1/interviews",
        json={
            "company_name": "GOOGLE",
            "role": "Backend Developer",
            "role_type": "Full-time",
            "status": "Rejected",
            "date_of_interview": "2026-10-21",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["id"] is not None

    with Session(get_test_engine) as session:
        companies = session.exec(
            select(Company).where(
                column("name").in_(["Google", "GOOGLE", "google"])
            )
        ).all()

        assert len(companies) == 1
        assert companies[0].name == "google"

def test_create_interview_feedback_with_sql_like_text(client, get_test_engine):
    payload = {
            "company_name": "Google",
            "role": "Backend Developer",
            "role_type": "Full-time",
            "status": "Rejected",
            "date_of_interview": "2026-10-21",
            }
    payload["feedback"] = "' OR '1'='1"

    response = client.post("/api/v1/interviews", json=payload)

    assert response.status_code == 201
    with Session(get_test_engine) as session:
            feedback = session.exec(
                select(InterviewFeedback)).all()
    
            assert len(feedback) == 1
            assert feedback[0].feedback == "' OR '1'='1"

