import asyncio
import httpx

from app.infrastructure.ergast.mappers import map_race

BASE_URL = "https://api.jolpi.ca/ergast/f1"

async def test_integration():
    season = 2023
    round_num = 1
    url = f"{BASE_URL}/{season}/{round_num}/results.json"
    
    print(f"Getting data from: {url}")
    
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(url)
        
        if response.status_code != 200:
            print(f"API error: {response.status_code}")
            return

        data = response.json()
        
        try:
            races_list = data['MRData']['RaceTable']['Races']
            if not races_list:
                print("API returned empty list of races.")
                return
                
            raw_race_data = races_list[0]
            
            print("Data downloaded. Mapping ...")
            
            race_domain_object = map_race(raw_race_data)
            
            print("\nSuccess! Domain object created:")
            print(f"Races: {race_domain_object.race_name} ({race_domain_object.date})")
            print(f"Winner: {race_domain_object.results[0].driver.family_name}")
            print(f"Number of results: {len(race_domain_object.results)}")
            
            print(f"Circuit: {race_domain_object.circuit.official_name}")
            print(f"Circuit country: {race_domain_object.circuit.country}")
            
        except KeyError as e:
            print(f"JSON structure error (Jolpica changed something?): {e}")
        except Exception as e:
            print(f"Mapper error: {e}")

if __name__ == "__main__":
    asyncio.run(test_integration())
