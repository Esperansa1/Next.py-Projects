class UsernameContainsIllegalCharacter(Exception):
    """Exception raised when a username contains an illegal character."""
    def __init__(self, username, letter):
        self.username = username
        self.message = f"Username '{username}' contains illegal character '{letter}'"
        super().__init__(self.message)

class UsernameTooShort(Exception):
    """Exception raised when a username is too short."""
    def __init__(self, username):
        self.username = username
        self.message = f"Username '{username}' is too short (minimum length is 3 characters)."
        super().__init__(self.message)

class UsernameTooLong(Exception):
    """Exception raised when a username is too long."""
    def __init__(self, username):
        self.username = username
        self.message = f"Username '{username}' is too long (maximum length is 16 characters)."
        super().__init__(self.message)

class PasswordTooShort(Exception):
    """Exception raised when a password is too short."""
    def __init__(self, password):
        self.password = password
        self.message = f"Password '{password}' is too short (minimum length is 8 characters)."
        super().__init__(self.message)

class PasswordTooLong(Exception):
    """Exception raised when a password is too long."""
    def __init__(self, password):
        self.password = password
        self.message = f"Password '{password}' is too long (maximum length is 40 characters)."
        super().__init__(self.message)

class PasswordMissingCharacter(Exception):
    """Base class for exceptions related to missing characters in a password."""
    def __init__(self, password):
        self.password = password
        self.message = f"Password '{password}' is missing a charachter "
        super().__init__(self.message)
    
    def __str__(self):
       return self.message

class PasswordMissingUppercase(PasswordMissingCharacter):
    """Exception raised when a password is missing an uppercase character."""
    def __str__(self):
        return super().__str__() + "(Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    """Exception raised when a password is missing a lowercase character."""
    def __str__(self):
        return super().__str__() + "(Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    """Exception raised when a password is missing a digit."""
    def __str__(self):
        return super().__str__() + "(Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    """Exception raised when a password is missing a special character."""
    def __str__(self):
        return super().__str__() + "(Special)"


def check_input(username, password):
    """Checks if the given username and password meet the requirements and raises appropriate exceptions."""
    if len(username) < 3:
        raise UsernameTooShort(username)

    if len(username) > 16:
        raise UsernameTooLong(username)

    if len(password) < 8:
        raise PasswordTooShort(password)
    
    if len(password) > 40:
        raise PasswordTooLong(password)
    
    english_lower = "abcdefghijklmnopqrstuvwxyz"
    english_upper = english_lower.upper()
    numbers = "1234567890"
    allowed_letters = english_lower + english_upper + numbers + "_"

    punctuation = "!@#$%^&*()_+-=.,/"

    for letter in username:
        if letter not in allowed_letters:
            raise UsernameContainsIllegalCharacter(username, letter)

    has_upper = False
    has_lower = False
    has_digit = False
    has_punct = False

    for letter in password:
        if letter in english_upper:
            has_upper = True
        elif letter in english_lower:
            has_lower = True
        elif letter in numbers:
            has_digit = True
        elif letter in punctuation:
            has_punct = True
    
    if not has_upper:
        raise PasswordMissingUppercase(password)

    if not has_lower:
        raise PasswordMissingLowercase(password)
    
    if not has_digit:
        raise PasswordMissingDigit(password)
    
    if not has_punct:
        raise PasswordMissingSpecial(password)

    return True