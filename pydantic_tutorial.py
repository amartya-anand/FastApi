from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):  # Pydantic class
    name: str = Field(max_length=50)
    age: int
    email: EmailStr
    weight: float = Field(gt=0)
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data inserted successfully.")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data updated successfully.")


patient_info = {'name': 'Amartya', 'age': 26, 'email': 'abcgmail.com', 'weight': 68, 'allergies': [
    'Pollen', 'Dust'], 'contact_details': {'phone': '123'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
