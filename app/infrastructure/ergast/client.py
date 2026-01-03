import httpx
from app.domain.models.race import Race
from .mappers import map_race
from app.domain.exceptions import ResourceNotFound, ExternalApiError

class ErgastClient:
    
    BASE_URL = "https://api.jolpi.ca/ergast/f1"

    async def get_results(self, season: int, round: int) -> Race:

        url = f"{self.BASE_URL}/{season}/{round}/results.json"

        async with httpx.AsyncClient(follow_redirects=True) as client:
            try: 
                response = await client.get(url, timeout=10)

                if response.status_code == 404:
                    raise ResourceNotFound(f"Race {season} round {round} not found.")
                
                response.raise_for_status()
            
            except httpx.HTTPStatusError as e:
                print(f"CRITICAL: API Error {e.response.status_code} for URL {url}")
                raise ExternalApiError(f"External service failed with status {e.response.status_code}") from e

            except httpx.RequestError as e:
                # network errors
                print(f"CRITICAL: Network Error accessing {url}: {e}")
                raise ExternalApiError("Network connection failed") from e

            try:
                data = response.json()
                races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])

                if not races:
                    raise ResourceNotFound(f"Race {season} round {round} data is empty.")

                return map_race(races[0])
            
            except (KeyError, IndexError, ValueError) as e:
                print(f"CRITICAL: Data Mapping Error: {e}")
                raise ExternalApiError("Invalid data format received from API") from e
