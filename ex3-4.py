import string
from functools import reduce

EXAMPLE_OF_ALPHA_CHAR = 'a'
MIN_USERNAME_LEN = 3
MAX_USERNAME_LEN = 16
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 40


class UsernameContainsIllegalCharacter(Exception):
    """ This error means that the username contains an illegal character for a username"""

    def __init__(self, illegal_chars, index):
        self._illegal_chars = illegal_chars
        self._index = index

    def __str__(self):
        return "The username contains an illegal character: {} at index {}".format(self._illegal_chars, self._index)


class UsernameTooShort(Exception):
    """ This error means that the username length is too short"""

    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    """ This error means that the username length is too long"""

    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    """ This error means that the password does not contain a certain type character"""

    def __str__(self):
        return "The password is missing a character "


class PasswordMissingUppercase(PasswordMissingCharacter):
    """ This error means that the password does not contain an uppercase type character"""

    def __str__(self):
        return super().__str__() + "(Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    """ This error means that the password does not contain a lowercase type character"""

    def __str__(self):
        return super().__str__() + "(Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    """ This error means that the password does not contain a digit type character"""

    def __str__(self):
        return super().__str__() + "(Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    """ This error means that the password does not contain a special type character"""

    def __str__(self):
        return super().__str__() + "(Special)"


class PasswordTooShort(Exception):
    """ This error means that the password length is below minimum length"""

    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    """ This error means that the password length is above maximum length"""

    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    """
    checks if credentials suit the custom specifications created
    :param username: the username
    :type username: str
    :param password: the password
    :type password: str
    :raises PasswordTooLong
    :raises PasswordTooShort
    :raises PasswordMissingSpecial
    :raises PasswordMissingDigit
    :raises PasswordMissingLowercase
    :raises PasswordMissingUppercase
    :raises UsernameTooLong
    :raises UsernameTooShort
    :raises UsernameContainsIllegalCharacter
    """
    # checks if username is made out of only alphabetical or numeric characters or underscores
    if username != "" and not username.replace("_", EXAMPLE_OF_ALPHA_CHAR).isalnum():
        # returns the last illegal character's index
        illegal_index = reduce(lambda x, y: y if not username[y].isalnum() and username[y] != "_" else x,
                               range(len(username)), -1)
        raise UsernameContainsIllegalCharacter(username[illegal_index], illegal_index)

    elif len(username) < MIN_USERNAME_LEN:
        raise UsernameTooShort

    elif len(username) > MAX_USERNAME_LEN:
        raise UsernameTooLong

    # There is an error in the question writing: it's said to keep the precedence of exception throwing identical to the
    # order they were given in the question but in the example the order is like I implemented here which is different
    # from the order in which the question is written

    elif len(password) < MIN_PASSWORD_LEN:
        raise PasswordTooShort

    elif len(password) > MAX_PASSWORD_LEN:
        raise PasswordTooLong

    elif not len([letter for letter in password if letter.isupper()]) > 0:
        raise PasswordMissingUppercase

    elif not len([letter for letter in password if letter.islower()]) > 0:
        raise PasswordMissingLowercase

    elif not len([letter for letter in password if letter.isnumeric()]) > 0:
        raise PasswordMissingDigit

    elif not len([letter for letter in password if letter in string.punctuation]) > 0:
        raise PasswordMissingSpecial

    print("OK")


def main():

    while True:
        username = input("please enter username ")
        password = input("please enter password ")

        try:
            check_input(username, password)

        except Exception as e:
            print(e.__str__())

        else:
            break


if __name__ == '__main__':
    main()
