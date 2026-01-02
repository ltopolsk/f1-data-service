import datetime
from pydantic import BaseModel, field_validator

from typing import Optional, List

from .driver import Driver
from .team import Team
from .circuit import Circuit 

class RaceResult(BaseModel):
    
    position: int
    points: float       # driver can get half points, check Belgium GP 2021
    grid: int
    laps: int           # not every driver completes all laps
    status: str         # "Finished", "Colision", "Disqualified", etc.
    time: Optional[str] = None

    driver: Driver
    constructor: Team


class Race(BaseModel):
    
    season: str
    round: int
    url: str
    race_name: str
    date: datetime.date
    time: Optional[str] = None
    circuit: Circuit
    results: List[RaceResult] = []

    @field_validator('results', mode='after')
    @classmethod
    def sort_results_by_position(cls, v: List[RaceResult]) -> List[RaceResult]:
        """
            Ensure that results are sorted by position
        """
        return sorted(v, key=lambda result: result.position)