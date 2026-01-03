from pydantic import BaseModel


class Constructor(BaseModel):

    constructor_id: str
    name: str
    nationality: str
    url: str
