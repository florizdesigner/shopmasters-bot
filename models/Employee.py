from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json()
@dataclass
class Employee:
    first_name: str
    last_name: str
    telegram_id: int
    telegram_username: str
    is_fulltime: bool
    work_group: int
    type_of_fulltime_shifts: int | None = None
    is_absence: bool = False