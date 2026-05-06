import strawberry

from db.database import SessionLocal

from schema.types import User
from schema.inputs import (
    CreateUserInput,
    UpdateUserInput
)

from services.user import UserService




@strawberry.type
class Mutation:

    def __init__(self):
        self.user_service = UserService()

    @strawberry.mutation
    def create_user(
        self,
        input: CreateUserInput
    ) -> User:

        db = SessionLocal()

        try:

            user = self.user_service.create_user(
                db,
                input.name,
                input.email
            )

            return User(
                id=user.id,
                name=user.name,
                email=user.email
            )

        finally:
            db.close()

    @strawberry.mutation
    def update_user(
        self,
        id: int,
        input: UpdateUserInput
    ) -> User:

        db = SessionLocal()

        try:

            user = self.user_service.update_user(
                db,
                id,
                input
            )

            return User(
                id=user.id,
                name=user.name,
                email=user.email
            )

        finally:
            db.close()

    @strawberry.mutation
    def delete_user(
        self,
        id: int
    ) -> User:

        db = SessionLocal()

        try:

            user = self.user_service.delete_user(
                db,
                id
            )

            return User(
                id=user.id,
                name=user.name,
                email=user.email
            )

        finally:
            db.close()