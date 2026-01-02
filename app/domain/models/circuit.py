from pydantic import BaseModel


class Circuit(BaseModel):

    official_name: str
    short_name: str
    country: str
    country_code: str
    url: str
