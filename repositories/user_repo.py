from sqlalchemy.orm import Session

from db.models import UserModel


class UserRepository:

    def get_all_users(
        self,
        db: Session
    ):
        return db.query(UserModel).all()

    def get_user_by_id(
        self,
        db: Session,
        user_id: int
    ):
        return (
            db.query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )

    def create_user(
        self,
        db: Session,
        name: str,
        email: str
    ):
        user = UserModel(
            name=name,
            email=email
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user

    def delete_user(
        self,
        db: Session,
        user
    ):
        db.delete(user)

        db.commit()