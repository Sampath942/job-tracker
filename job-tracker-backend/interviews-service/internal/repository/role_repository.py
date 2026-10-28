
from sqlmodel import Session, select
from internal.models.role import Role

def get_or_create_role(session: Session, role: str) -> Role:
    # Check if the role already exists in the database
    statement = select(Role).where(Role.name == role)

    existing_role = session.exec(statement).first()
    if existing_role:
        return existing_role

    # If the role doesn't exist, create a new one
    new_role = Role(name=role)
    session.add(new_role)
    session.flush() 
    return new_role