from typing import Any
from enum import Enum
from datetime import datetime
from pydantic import (BaseModel,
                      Field,
                      ValidationError,
                      model_validator)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=20)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def safety_validator(mission) -> Any:
        def experienced_crew(crew: list[CrewMember]) -> bool:
            half_crew = len(crew) / 2
            exp_crew = 0
            for member in crew:
                if member.years_experience > 5:
                    exp_crew += 1
            if exp_crew >= half_crew:
                return True
            return False

        if not mission.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(
            member.rank in [Rank.COMMANDER, Rank.CAPTAIN]
            for member in mission.crew
        ):
            raise ValueError("Mission must have at least one Commander or"
                             " Captain")
        if mission.duration_days > 365 and not experienced_crew(mission.crew):
            raise ValueError("Long missions require at least 50% "
                             " experienced crew.")
        for member in mission.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return mission


def print_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}\n"
          f"ID: {mission.mission_id}\n"
          f"Destination: {mission.destination}\n"
          f"Duration: {mission.duration_days} days\n"
          f"Budget: ${mission.budget_millions}M\n"
          f"Crew size: {len(mission.crew)}\n"
          f"Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")


def main() -> None:
    mission = SpaceMission(
        mission_name="Solar Observatory Research Mission",
        mission_id="M2024_TITAN",
        destination="Solar Observatory",
        launch_date=datetime(2024, 3, 30),
        duration_days=451,
        budget_millions=2208.1,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Williams",
                rank=Rank.CAPTAIN,
                age=43,
                specialization="Mission Command",
                years_experience=19
            ),
            CrewMember(
                member_id="L01",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=6
            ),
            CrewMember(
                member_id="O01",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=24,
                specialization="Engineering",
                years_experience=2
            )
        ]
    )

    print("\nSpace Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    nuevo_miembro = CrewMember(
                    member_id="C01",
                    name="Sarah Connor",
                    rank=Rank.CAPTAIN,
                    age=34,
                    specialization="Mission Command",
                    years_experience=6,
                    is_active=True
                )
    print_mission(mission)
    print("\n=========================================")
    print("Expected validation error:")
    try:
        mission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C01",
                    name="Sarah Connor",
                    rank=Rank.CAPTAIN,
                    age=34,
                    specialization="Mission Command",
                    years_experience=3,
                    is_active=True
                ),
                nuevo_miembro,
                CrewMember(
                    member_id="O01",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=24,
                    specialization="Engineering",
                    years_experience=3
                )
            ],
            launch_date=datetime(2024, 3, 25)
        )
        print_mission(mission)
    except ValidationError as err:
        for error in err.errors():
            print(f"{error['msg']}\n")


if __name__ == "__main__":
    main()
