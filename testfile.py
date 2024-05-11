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

employee_json = {
    "first_name": "Ivan",
    "last_name": "Petrov",
    "telegram_id": 123123123,
    "telegram_username": "abobobboobob",
    "is_fulltime": True,
    "work_group": 1,
    "type_of_fulltime_shifts": 1
}

print(Employee.from_dict(employee_json).to_dict())