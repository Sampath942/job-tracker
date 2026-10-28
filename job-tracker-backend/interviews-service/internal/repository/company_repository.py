
from sqlmodel import Session, select
from internal.models.company import Company

def get_or_create_company(session: Session, company_name: str) -> Company:
    # Check if the company already exists in the database
    statement = select(Company).where(Company.name == company_name)

    existing_company = session.exec(statement).first()
    if existing_company:
        return existing_company

    # If the company doesn't exist, create a new one
    new_company = Company(name=company_name)
    session.add(new_company)
    session.flush() 
    return new_company