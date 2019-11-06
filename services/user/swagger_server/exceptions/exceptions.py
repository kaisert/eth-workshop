class UserNotFoundException(Exception):
    def __init__(self):
        pass


class UserAlreadyExistsException(Exception):
    pass
