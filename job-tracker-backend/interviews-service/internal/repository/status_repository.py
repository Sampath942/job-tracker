from sqlmodel import Session, select
from internal.models.status import Status

def get_or_create_status(session: Session, status: str) -> Status:
    # Check if the status already exists in the database
    statement = select(Status).where(Status.name == status)

    existing_status = session.exec(statement).first()
    if existing_status:
        return existing_status

    # If the status doesn't exist, create a new one
    new_status = Status(name=status)
    session.add(new_status)
    session.flush() 
    return new_status