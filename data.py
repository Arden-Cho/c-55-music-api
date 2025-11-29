import datetime
from dataclasses import dataclass


@dataclass
class Music:
    music_id: int
    title: str
    date: datetime.date
    author: str


@dataclass(frozen=True)
class Reminder:
    reminder_id: int
    hour: int
    minute: int
    music_id: int
    enabled: bool


MUSIC_LIST: list[Music] = [
    Music(music_id=0, title="That's Why I Gave Up on Music", date=datetime.date(2019, 4, 10), author="ヨルシカ"),
    Music(music_id=1, title="Elma", date=datetime.date(2019, 4, 10), author="ヨルシカ"),
    Music(music_id=2, title="Amy", date=datetime.date(2019, 8, 28), author="ヨルシカ"),
    Music(music_id=3, title="Rain with Cappuccino", date=datetime.date(2019, 8, 28), author="ヨルシカ"),
]

REMINDERS_DEFAULT_LIST: list[Reminder] = [
    Reminder(reminder_id=0, hour=12, minute=30, music_id=1, enabled=True),
    Reminder(reminder_id=1, hour=1, minute=58, music_id=3, enabled=False),
    Reminder(reminder_id=2, hour=18, minute=21, music_id=2, enabled=True),
    Reminder(reminder_id=3, hour=9, minute=20, music_id=3, enabled=True),
    Reminder(reminder_id=4, hour=20, minute=5, music_id=0, enabled=False),
]
