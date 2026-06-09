from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200, default=None)


def print_station(station: SpaceStation) -> None:
    print(f"ID: {station.station_id}\n"
          f"Name: {station.name}\n"
          f"Crew: {station.crew_size} people\n"
          f"Power: {station.power_level}%\n"
          f"Oxygen: {station.oxygen_level}%\n"
          f"Last Maintenance: {station.last_maintenance}\n"
          "Status: "
          f"{'Operational' if station.is_operational else '[ERROR]'}\n")
    if station.notes is not None:
        print(f"Notes: {station.notes}")


def main() -> None:
    print("\nSpace Station Data Validation\n"
          "========================================")
    station = SpaceStation(
        station_id="ISS674",
        name="Europa Research Station",
        crew_size=3,
        power_level=70.8,
        oxygen_level=88.1,
        last_maintenance=datetime(2023, 8, 24),
        is_operational=False
    )
    print("Valid station created:")
    print_station(station)
    station = SpaceStation(
        station_id="ISS877",
        name="Mars Orbital Platform",
        crew_size=9,
        power_level=79.7,
        oxygen_level=87.2,
        last_maintenance=datetime(2023, 10, 6),
        is_operational=True,
        notes="System diagnostics required"
    )
    print("\nValid station created:")
    print_station(station)
    print("\n========================================")
    print("Expected validation error:")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=54,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2025, 1, 21),
            is_operational=True
        )
    except ValidationError as err:
        for error in err.errors():
            print(f"{error['msg']}\n")


if __name__ == "__main__":
    main()
