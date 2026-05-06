from graphql import GraphQLError

from repositories.user_repo import UserRepository


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def get_users(self, db):

        return self.user_repository.get_users(db)

    def get_user_by_id(
        self,
        db,
        user_id: int
    ):

        user = self.user_repository.get_user_by_id(
            db,
            user_id
        )

        if user is None:
            raise GraphQLError(
                f"User with id {user_id} not found"
            )

        return user

    def create_user(
        self,
        db,
        name: str,
        email: str
    ):

        existing_user = (
            self.user_repository.get_user_by_email(
                db,
                email
            )
        )

        if existing_user:
            raise GraphQLError(
                "User with this email already exists"
            )

        return self.user_repository.create_user(
            db,
            name,
            email
        )

    def update_user(
        self,
        db,
        user_id: int,
        input
    ):

        user = self.user_repository.get_user_by_id(
            db,
            user_id
        )

        if user is None:
            raise GraphQLError(
                f"User with id {user_id} not found"
            )

        if input.email is not None:

            existing_user = (
                self.user_repository.get_user_by_email(
                    db,
                    input.email
                )
            )

            if (
                existing_user
                and existing_user.id != user_id
            ):
                raise GraphQLError(
                    "Email already in use"
                )

        if input.name is not None:
            user.name = input.name

        if input.email is not None:
            user.email = input.email

        return self.user_repository.save(
            db,
            user
        )

    def delete_user(
        self,
        db,
        user_id: int
    ):

        user = self.user_repository.get_user_by_id(
            db,
            user_id
        )

        if user is None:
            raise GraphQLError(
                f"User with id {user_id} not found"
            )

        self.user_repository.delete_user(
            db,
            user
        )

        return user