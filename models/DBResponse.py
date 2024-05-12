from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json()
@dataclass
class DBResponse:
    status: str
    message: str | None = None
    employee: object | None = None