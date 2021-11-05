from pydantic import BaseModel

class SampleSchema(BaseModel):
    firstname: str
    lastname: str
