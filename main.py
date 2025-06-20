from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

app = FastAPI()  # app object


class Patient(BaseModel):
    id: Annotated[
        str,
        Field(..., description='ID of the patient', examples=["P0001"])
    ]
    name: Annotated[str, Field(..., description='Name of the patient', examples=[
                               "John Doe"])]
    city: Annotated[str, Field(..., description='City of the patient', examples=[
                               "New York"])]
    age: Annotated[int, Field(..., gt=0, lt=100,
                              description='Age of the patient', examples=[30])]
    gender: Annotated[Literal['M', 'F', 'Others'],
                      Field(..., description='Gender of the patient')]
    height: Annotated[float,
                      Field(..., gt=0, description='Height of the patient in m')]
    weight: Annotated[float,
                      Field(..., gt=0, description='Weight of the patient in kg')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal weight'
        else:
            return 'Overweight'


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['M', 'F', 'Others']],
                      Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():  # Helper function
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


@app.get("/")  # Decorator
def hello():
    return {'message': 'Patient Management System API'}


@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage your system records'}


@app.get('/view')
def view():
    data = load_data()
    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient in the DB", example="P0001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of Height and Weight or BMI'), order=Query("asc", description='Sort in ascending or descending order')):
    valid_fields = ['Height', 'Weight', 'BMI']
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f'Invalid field selected from {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400, detail='Order must be either asc or desc')
    data = load_data()
    sort_order = True if order == 'asc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(
        sort_by), reverse=sort_order)
    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

        existing_patient_info = data[patient_id]
        # Model dump transforms the object into a dictionary
        updated_patient_info = patient.update.model_dump(
            exclude_unset=True)  # Not all the values need to be updated

        for key, value in updated_patient_info.items():
            existing_patient_info[key] = value

            existing_patient_info['id'] = patient_id
            patient_pydantic_obj = Patient(**existing_patient_info)
            existing_patient_info = patient_pydantic_obj.model_dump(exclude=[
                'id'])
            data[patient_id] = existing_patient_info

            save_data(data)
            return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})
