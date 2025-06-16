from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()  # app object


def load_data():  # Helper function
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


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
# Path is increasing the readibility
def view_patient(patient_id: str = Path(..., description="The ID of the patient in th DB", example="P0001")):
    # Load patient data
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
