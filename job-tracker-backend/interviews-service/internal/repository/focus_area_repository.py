from sqlmodel import Session, select
from internal.models.focusarea import FocusArea

def get_or_create_focus_area(session: Session, focus_area_name: str) -> FocusArea:
    # Check if the focus area already exists in the database
    statement = select(FocusArea).where(FocusArea.name == focus_area_name)

    existing_focus_area = session.exec(statement).first()
    if existing_focus_area:
        return existing_focus_area

    # If the focus area doesn't exist, create a new one
    new_focus_area = FocusArea(name=focus_area_name)
    session.add(new_focus_area)
    session.flush() 
    return new_focus_area