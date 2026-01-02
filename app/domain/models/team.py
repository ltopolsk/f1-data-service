from pydantic import BaseModel


class Team(BaseModel):

    constructor_id: str
    name: str
    nationality: str
    url: str
