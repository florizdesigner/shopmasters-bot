from dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.Employee import EmployeeResponse


@dataclass_json()
@dataclass
class DBResponse:
    status: str
    message: str | None = None
    employee: object | None = None