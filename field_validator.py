from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):  # Pydantic class
    name: str
    age: int
    email: EmailStr
    weight: float
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com',]
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    # Mode decide whether to compare befor or after type conversion,default mode is after
    @field_validator('age', mode='after')
    @classmethod
    def validator_age(cl, value):
        if 0 < value < 100:
            return value
        else:
            return ValueError('Age should be in range between 0 and 100')


patient_info = {'name': 'Amartya', 'age': '26', 'email': 'abc@icici.com', 'weight': 68, 'allergies': [
    'Pollen', 'Dust'], 'contact_details': {'phone': '123'}}

patient1 = Patient(**patient_info)


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print("Patient data updated successfully.")


update_patient_data(patient1)
