from uuid import UUID
from sqlalchemy.orm import Session
# from fastapi import HTTPException
from . import model
from src.entities.user import User
from src.exceptions import UserNotFoundError, InvalidPasswordError, PasswordMismatchError
from src.auth.service import verify_password, get_password_hash
import logging

def get_user_by_id(db: Session, user_id: UUID) -> model.UserResponse:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logging.warning(f"User not found with ID: {user_id}")
        raise UserNotFoundError(user_id)
    logging.info(f"Successfully retrieved user with ID: {user_id}")
    return user

def change_password(db: Session, user_id: UUID, password_change: model.PasswordChange) -> None:
    try:
        user = get_user_by_id(db, user_id)

        if not verify_password(password_change.current_password, user.password_hash):
            logging.warning(f"Invalid current password for user ID: {user_id}")
            raise InvalidPasswordError()

        if password_change.new_password != password_change.new_password_confirm:
            logging.warning(f"Password mismatch for user ID: {user_id}")
            raise PasswordMismatchError()

        user.password_hash = get_password_hash(password_change.new_password)
        db.commit()
        logging.info(f"Successfully changed password for user ID: {user_id}")

    except Exception as e:
        logging.error(f"Error changing password for user ID {user_id}: {str(e)}")
        raise