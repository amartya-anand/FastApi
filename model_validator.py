from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):  # Pydantic class
    name: str
    age: int
    email: EmailStr
    weight: float
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='before')
    def validate_emergency_contact(cls, model):
        if int(model.get('age', 0)) > 60 and 'emergency' not in model.get('contact_details', {}):
            raise ValueError(
                "Emergency contact is required for patients over 60 years old.")
        return model


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data updated successfully.")


patient_info = {'name': 'Amartya', 'age': '26', 'email': 'abc@icici.com', 'weight': 68, 'allergies': [
    'Pollen', 'Dust'], 'contact_details': {'phone': '123'}, 'emergency': '123456789'}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
