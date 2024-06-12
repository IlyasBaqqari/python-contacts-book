import re

def validate_id(id: str) -> bool:
    if not id.isdigit():
        print('\n** Input Invalid **')
        print('ID entered must be an integer...\n')
        return False
    # If valid
    return True


def validate_phone(phone: str) -> bool:
    if not phone.isdigit() or len(phone) > 11:
        print('\n** Input Invalid **')
        print('Phone number entered must be a valid UK phone number...\n')
        return False
    # If valid
    return True


def validate_email(email: str) -> bool:
    if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print('\n** Input Invalid **')
        print('Email entered must be valid email address...\n')
        return False
    # If valid
    return True


def validate_postcode(postcode: str) -> bool:
    if not re.match('([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})', postcode):
        print('\n** Input Invalid **')
        print('Postcode entered must be a valid UK postcode...\n')
        return False
    # If valid
    return True


