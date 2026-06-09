from typing import Any
from enum import Enum
from datetime import datetime
from pydantic import (BaseModel,
                      Field,
                      ValidationError,
                      model_validator)


class ContactType(Enum):
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
    VISUAL = "visual"
    RADIO = "radio"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_rules(a_contact) -> Any:
        if not a_contact.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        if (a_contact.contact_type == ContactType.PHYSICAL
           and not a_contact.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (a_contact.contact_type == ContactType.TELEPATHIC
           and a_contact.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3"
                             " witnesses")
        if (a_contact.signal_strength > 7.0
                and not a_contact.message_received):
            raise ValueError("Strong signals (>7.0) must include a received"
                             " message")
        return a_contact


def print_report(contact: AlienContact) -> None:
    print(f"ID: {contact.contact_id}\n"
          f"Type: {contact.contact_type.value}\n"
          f"Location: {contact.location}\n"
          f"Timestamp: {contact.timestamp}\n"
          f"Signal: {contact.signal_strength}/10\n"
          f"Duration: {contact.duration_minutes} minutes\n"
          f"Witnesses: {contact.witness_count}\n"
          f"Message: '{contact.message_received}'\n"
          f"Verified: '{contact.is_verified}'\n")


def main() -> None:
    contact = AlienContact(
        contact_id='AC_2024_001',
        timestamp=datetime(2024, 1, 20),
        location='Atacama Desert, Chile',
        contact_type=ContactType.VISUAL,
        signal_strength=9.6,
        duration_minutes=99,
        witness_count=11,
        message_received='Greetings from Zeta Reticuli',
        is_verified=False
    )
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print_report(contact)
    contact = AlienContact(
        contact_id="AC_2024_007",
        timestamp=datetime(2024, 3, 25),
        location="Mauna Kea Observatory, Hawaii",
        contact_type=ContactType.PHYSICAL,
        signal_strength=9.0,
        duration_minutes=138,
        witness_count=10,
        message_received="Request for peaceful contact",
        is_verified=True
    )
    print("Valid contact report:")
    print_report(contact)
    print("\n========================================")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            timestamp=datetime(2025, 1, 21)
        )
    except ValidationError as err:
        for error in err.errors():
            print(f"{error['msg']}\n")


if __name__ == "__main__":
    main()
