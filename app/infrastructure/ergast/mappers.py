from app.domain.models.race import Race, RaceResult
from app.domain.models.driver import Driver
from app.domain.models.constructor import Constructor
from app.domain.models.circuit import Circuit
import datetime


def map_driver(raw_driver_data: dict) -> Driver:
    return Driver(
        driver_id=raw_driver_data['driverId'],
        driver_number=int(raw_driver_data['permanentNumber']),
        code=raw_driver_data.get('code'),
        url=raw_driver_data.get('url'),
        given_name=raw_driver_data['givenName'],
        family_name=raw_driver_data['familyName'],
        date_of_birth=datetime.date.fromisoformat(raw_driver_data['dateOfBirth']),
        nationality=raw_driver_data['nationality']
    )


def map_constructor(raw_constructor_data: dict) -> Constructor:
    return Constructor(
        constructor_id=raw_constructor_data['constructorId'],
        name=raw_constructor_data['name'],
        nationality=raw_constructor_data['nationality'],
        url=raw_constructor_data.get('url')
    )


def map_circuit(raw_circuit_data: dict) -> Circuit:
    return Circuit(
        official_name=raw_circuit_data['circuitName'],
        short_name=raw_circuit_data['circuitId'],
        country=raw_circuit_data.get('Location', {}).get('country', 'Unknown'),
        url=raw_circuit_data['url']
    )


def map_race(raw_race_data: dict) -> Race:

    results = []

    raw_results = raw_race_data.get('Results', [])

    for result in raw_results:
        driver = map_driver(result['Driver'])
        constructor = map_constructor(result['Constructor'])

        time_str = None
        if result.get('Time'):
            time_str = result['Time'].get('time')

        r = RaceResult(
            position=int(result['position']),
            points=float(result['points']),
            grid=int(result['grid']),
            laps=int(result['laps']),
            status=result['status'],
            time=time_str,
            driver=driver,
            constructor=constructor,
        )
        results.append(r)

    circuit = map_circuit(raw_race_data['Circuit'])

    race_time = None
    if raw_race_data.get('time'):
        race_time = raw_race_data['time'].rstrip('Z')
        # try:
        #     race_time = datetime.time.fromisoformat(clean_time)
        # except ValueError:
        #     pass # Or log parsing error

    return Race(
        race_name=raw_race_data['raceName'],
        season=int(raw_race_data['season']),
        round=int(raw_race_data['round']),
        url=raw_race_data['url'],
        date=datetime.date.fromisoformat(raw_race_data['date']),
        time=race_time,
        results=results,
        circuit=circuit
    )
