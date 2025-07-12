# this is my pydantic model to make sure the input and return is welll structred
from pydantic import BaseModel,Emailstr
from datetime import datetime
class User(BaseModel):
    username:str
    email:Emailstr

class UserIn(User):
    password:str

class UserOut(User):
    pass


class Tenat(BaseModel):
    name:str
    start_date:datetime
    end_date:datetime
    phone_number:
    signed:datetime

class Payment(Tenat):
    rent:
    date:datetime
    months:str

