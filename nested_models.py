from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    # age: int
    address: Address


address_dict = {'city': 'Pune', 'state': 'Maharashtra', 'pin': '411001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Amartya', 'gender': 'M', 'address': address1}

pateint1 = Patient(**patient_dict)

print(pateint1)
print(pateint1.address)
print(pateint1.address.city)
