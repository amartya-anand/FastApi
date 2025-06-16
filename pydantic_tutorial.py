from pydantic import BaseModel
from typing import List, Dict, Optional


class Patient(BaseModel):  # Pydantic class
    name: str
    age: int
    weight: float
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


patient_info = {'name': 'Amartya', 'age': 26, 'weight': 68, 'allergies': [
    'Pollen', 'Dust'], 'contact_details': {'e-mail': 'abc@gmail.com', 'phone': '123'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
