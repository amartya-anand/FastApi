from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):  # Pydantic class
    name: str
    age: int
    email: EmailStr
    weight: float  # Weight in kg
    height: float  # Height in meters
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data updated successfully.")
    print("BMI", patient.bmi)


patient_info = {'name': 'Amartya', 'age': '26', 'email': 'abc@icici.com', 'weight': 75.2, 'height': 1.72, 'allergies': [
    'Pollen', 'Dust'], 'contact_details': {'phone': '123'}}

patient1 = Patient(**patient_info)


update_patient_data(patient1)
