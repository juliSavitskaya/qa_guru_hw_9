from dataclasses import dataclass
from enum import Enum
import datetime


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobby(Enum):
    SPORTS = "Sports"
    MUSIC = "Music"
    READING = "Reading"


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone: str
    birth_date: datetime.date
    address: str
    picture: str
    hobby: Hobby
    subjects: list[str] = None
    state: str = ""
    city: str = ""


student = User(
    first_name="Ivan",
    last_name="Ivanov",
    email="ivanov@fake.com",
    gender=Gender.MALE,
    phone="9555555555",
    birth_date=datetime.date(1995, 5, 20),
    address="Test address",
    picture="tests/test1.jpeg",
    hobby=Hobby.SPORTS,
    subjects=["Physics"],
    state="NCR",
    city="Delhi"
)