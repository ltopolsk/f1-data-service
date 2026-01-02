from pydantic import BaseModel
from datetime import date


class Driver(BaseModel):

    driver_id: str
    driver_number: int
    code: str
    given_name: str
    family_name: str
    date_of_birth: date
    nationality: str
    url: str

    # Team
