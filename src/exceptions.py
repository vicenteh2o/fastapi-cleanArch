from fastapi import HTTPException

class TodoError(HTTPException):
    """Base exception for Todo-related errors."""
    pass

class TodoNotFoundError(TodoError):
    def __init__(self, todo_id=None):
        message = "Todo not found" if todo_id is None else f"Todo not found with id {todo_id}"
        super().__init__(status_code=404, detail=message)

class TodoCreationError(TodoError):
    def __init__(self, error: str):
        super().__init__(status_code=500, detail=f"Failed to create todo: {error}")

class UserError(HTTPException):
    """Base exception for User-related errors."""
    pass

class UserNotFoundError(UserError):
    def __init__(self, user_id=None):
        message = "User not found" if user_id is None else f"User not found with id {user_id}"
        super().__init__(status_code=404, detail=message)

class PasswordMismatchError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="Password does not match")

class InvalidPasswordError(UserError):
    def __init__(self):
        super().__init__(status_code=401, detail="Current password is incorrect")

class AuthenticationError(HTTPException):
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(status_code=401, detail=message)