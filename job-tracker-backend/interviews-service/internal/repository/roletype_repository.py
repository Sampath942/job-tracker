from sqlmodel import Session, select
from internal.models.roletype import RoleType

def get_or_create_roletype(session: Session, role_type: str) -> RoleType:
    # Check if the role type already exists in the database
    statement = select(RoleType).where(RoleType.name == role_type)

    existing_roletype = session.exec(statement).first()
    if existing_roletype:
        return existing_roletype

    # If the role type doesn't exist, create a new one
    new_roletype = RoleType(name=role_type)
    session.add(new_roletype)
    session.flush() 
    return new_roletype