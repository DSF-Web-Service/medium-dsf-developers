from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from schema import SampleSchema

app = FastAPI(title="Sample App")


@app.get("/")
async def get_data():
    data = SampleSchema(firstname="Cakra", lastname="Amiyantoro")
    return data

@app.get("/{id}")
async def get_data_detail(id: int):
    data = SampleSchema(firstname="Cakra", lastname="Amiyantoro")
    return data

@app.post("/")
async def create_data(request: SampleSchema):
    data = jsonable_encoder(request)
    data.update({"id": 1})
    return data

@app.put("/{id}")
async def update_data(id: int, request: SampleSchema):
    data = jsonable_encoder(request)
    data.update({"id": id})
    return data

@app.delete("/{id}")
async def delete_data(id: int):
    return {"message": f"The data with id {id} has been deleted."}