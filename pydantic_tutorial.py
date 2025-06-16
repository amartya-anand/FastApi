from pydantic import BaseModel


class Patient(BaseModel):  # Pydantic class
    name: str
    age: int


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")


patient_info = {'name': 'Amartya', 'age': 26}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
