from typing import Union
from .address import Address

class Contact:
    last_id = 0

    def __init__(self, id: Union[int, None], first_name: str, surname: str, phone_number: str, email: str, address: Address, increment_last_id: bool = True):
        # If no ID given, use last_id
        # Unless objected, increment last_id
        if id is None:
            self.id = Contact.last_id + 1
            if increment_last_id:
                Contact.last_id += 1
        else:
            self.id = id

        self.first_name = first_name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        underline = '-' * len(str(self.id) + ': ' + self.first_name + ' ' + self.surname)
        output = f'ID: {self.id}\n'

        if self.first_name or self.surname:
            if self.first_name:
                output += f'{self.first_name} '
            if self.surname:
                output += f'{self.surname}'
            output += f'\n{underline}'

        if self.phone_number or self.email:
            if self.phone_number:
                output += f'\nPhone: {self.phone_number}'
            if self.email:
                output += f'\nEmail: {self.email}'
            output += f'\n{underline}'

        if self.address:
            output += f'{self.address}'

        return output