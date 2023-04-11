"""Python module to know if a string is palindrome"""


def is_palindrome(string: str) -> bool:
    """Returns if the string is palindrome (True or False)"""

    string = string.replace(' ', '')
    string = string.lower()
    return string == string[::-1]


def run():
    print(is_palindrome('Hola mundo!'))


if __name__ == '__main__':
    run()