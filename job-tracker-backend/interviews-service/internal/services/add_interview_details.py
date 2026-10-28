from sqlmodel import Session

from internal.schemas.interview_create import InterviewCreate, InterviewRead
from internal.repository.company_repository import get_or_create_company
from internal.repository.interview_repository import create_interview
from internal.repository.interview_company_repository import create_interview_company
from internal.repository.role_repository import get_or_create_role
from internal.repository.interview_role_repository import create_interview_role
from internal.repository.roletype_repository import get_or_create_roletype
from internal.repository.interview_roletype_repository import create_interview_roletype
from internal.repository.status_repository import get_or_create_status
from internal.repository.interview_status_repository import create_interview_status
from internal.repository.focus_area_repository import get_or_create_focus_area
from internal.repository.interview_focus_area_repository import create_interview_focus_area
from internal.repository.interview_question_answer_repository import create_interview_question_answer
from internal.repository.interview_feedback_repository import create_interview_feedback

def to_lowercase(data: str) -> str:
    return data.strip().lower()

def add_interview_details_service(interview_data: InterviewCreate, session: 
                                  Session) -> InterviewRead:
    interview_data.company_name = to_lowercase(interview_data.company_name)
    interview_data.role = to_lowercase(interview_data.role)
    interview_data.role_type = to_lowercase(interview_data.role_type)
    interview_data.status = to_lowercase(interview_data.status)
    with session.begin():
        interview = create_interview(
            session=session, 
            interview_data=
                {
                    "date_of_interview": interview_data.date_of_interview, 
                    "job_link": interview_data.job_link
                })
        
        if interview.id is None:
            raise RuntimeError(
                "Interview ID was not generated after insertion"
            )

        company = get_or_create_company(
            session=session,
            company_name=interview_data.company_name,
        )

        if company.id is None:
            raise RuntimeError(
                "Company ID was not generated after insertion"
            )
        create_interview_company(
            session=session,
            interview_id=interview.id,
            company_id=company.id
        )

        role = get_or_create_role(
            session=session,
            role=interview_data.role,
        )

        if role.id is None:
            raise RuntimeError(
                "Role ID was not generated after insertion"
            )

        create_interview_role(
            session=session,
            interview_id=interview.id,
            role_id=role.id,
        )

        roletype = get_or_create_roletype(
            session=session,
            role_type=interview_data.role_type,
        )

        if roletype.id is None:
            raise RuntimeError(
                "Role Type ID was not generated after insertion"
            )

        create_interview_roletype(
            session=session,    
            interview_id=interview.id,
            roletype_id=roletype.id,
        )

        status = get_or_create_status(
            session=session,
            status=interview_data.status,
        )

        if status.id is None:
            raise RuntimeError(
                "Status ID was not generated after insertion"
            )

        create_interview_status(
            session=session,
            interview_id=interview.id,
            status_id=status.id,
        )

        for focus_area in interview_data.focus_areas:
            focus_area_obj = get_or_create_focus_area(
                session=session,
                focus_area_name=to_lowercase(focus_area),
            )

            if focus_area_obj.id is None:
                raise RuntimeError(
                    "Focus Area ID was not generated after insertion"
                )

            create_interview_focus_area(
                session=session,
                interview_id=interview.id,
                focus_area_id=focus_area_obj.id,
            )

        for question, answer in zip(interview_data.questions, interview_data.answers):
            create_interview_question_answer(
                session=session,
                interview_id=interview.id,
                question=question,
                answer=answer,
            )

        if interview_data.feedback:
            create_interview_feedback(
                session=session,
                interview_id=interview.id,
                feedback=interview_data.feedback,
            )

    return InterviewRead(id=interview.id) 