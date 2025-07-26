from fastapi import FastAPI

app = FastAPI()

tenats = [{
        "id" : 1,
        "name" : "John mui",
        "Date of sign":"2020-01-09",
        "End of rent" :"2020-03-31"
    },
    {
        "id" : 2,
        "name" : "JUI mui",
        "Date of sign":"2010-01-09",
        "End of rent" :"20210-03-31"
    },
]

@app.get("/")
def root():
    return{"message":"Welcome to my tenats"}

@app.get("/tenats")
def get_all_tenats():
    return tenats

@app.get("/tenats/{id}")
def get_tenat(id:int):
    for tenat in tenats:
        if tenat['id'] == id:
            return tenat
        

@app.post("/tenats")
def create_tenat(response:TenatCreat):

    new_id = max([t["id"] for t in tenats])

    new_tenat = {
        "id":new_id,
        "name":response.name,
        "Date of sign":response.date_of_sign,
        "End of rent":response.end_of_rent
    }
    tenats.append(new_tenat)
    return new_tenat



