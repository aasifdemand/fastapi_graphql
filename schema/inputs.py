import strawberry
from typing import Optional

@strawberry.input
class CreateUserInput:
    name: str
    email: str



@strawberry.input
class UpdateUserInput:
    name: Optional[str] = None
    email: Optional[str] = None