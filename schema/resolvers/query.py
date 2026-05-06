import strawberry

from db.database import SessionLocal

from schema.types import User

from services.user import UserService


user_service = UserService()


@strawberry.type
class Query:

    @strawberry.field
    def get_users(self) -> list[User]:

        db = SessionLocal()

        try:

            users = user_service.get_users(db)

            return [
                User(
                    id=user.id,
                    name=user.name,
                    email=user.email
                )
                for user in users
            ]

        finally:
            db.close()

    @strawberry.field
    def get_user_by_id(
        self,
        id: int
    ) -> User:

        db = SessionLocal()

        try:

            user = user_service.get_user_by_id(
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