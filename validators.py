import re

password_regex = "^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&]).{8,}$"


def password_is_valid(password):
    return bool(re.match(password_regex, password))
