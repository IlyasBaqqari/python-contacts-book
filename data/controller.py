import os, sys

sys.path.append('..')
from contacts import Contact, Address
from utils import validate_phone, validate_email, validate_postcode

from .database import DatabaseManager
class Controller:
    def __init__(self, db_url: str) -> None:
        self.db = DatabaseManager(db_url)
        self.db.init_table()

        contacts = self.db.get_all_contacts()
        if contacts:
            Contact.last_id = self.db.get_all_contacts()[-1].id
        else:
            Contact.last_id = 0


    def get_all_contacts(self) -> None:
        contacts = self.db.get_all_contacts()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('~~ View all Contacts ~~')
        print(f'Listing {len(contacts)} contact{'s' if len(contacts) != 1 else ''}...\n')

        for contact in contacts:
            print(f'{contact}\n')


    def get_contact(self, id: str) -> None:
        contact = self.db.get_contact_by_id(id)
        if contact:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'~~ Contact Found ~~\n\n{contact}\n')
        else:
            print('\n~~ No Contact Found ~~')
            print(f'No contact was found with ID {id}...\n')


    def new_contact(self) -> None:
        contact = self.enter_contact_details()
        self.db.insert_contact(contact)
        print('Contact created!')


    def update_contact(self, id: str) -> None:
        # Check exists
        old_contact = self.db.get_contact_by_id(id)
        if not old_contact:
            print('\n~~ No Contact Found ~~')
            print(f'No contact was found with ID {id}...\n')
        else:
            updated_contact = self.enter_contact_details(old_contact, 'update')
            self.db.update_contact(updated_contact)
            print('Contact updated!')


    def delete_contact(self, id: str) -> None:
        # Check exists
        contact = self.db.get_contact_by_id(id)
        if not contact:
            print('\n~~ No Contact Found ~~')
            print(f'No contact was found with ID {id}...\n')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('~~ Delete Contact ~~\n')
            print(f'{contact}\n')

            # Confirm deletion
            print('Once deleted, a contact cannot be recovered.')
            if input('Are you sure you want to delete this contact? (y/n) ➡ ').lower() == 'y':
                self.db.delete_contact(id)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Contact deleted!')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Operation cancelled.')


    def enter_contact_details(self, old_contact: Contact = None, operation: str = 'create') -> None:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            # If updating, show original
            if operation == 'update':
                print('~~ Updating Contact ~~')
                print(f'\n{old_contact}')

            # Show appropriate dialog
            if operation == 'create':
                print('~~ New Contact ~~')
            elif operation == 'update':
                print('\n~~ Updated Info ~~')

            print('* All fields are optional\n')

            fname = input('Firstname(s): ')
            sname = input('Surname(s): ')

            while True:
                phone = input('Phone number: ')
                if validate_phone(phone):
                    break

            while True:
                email = input('Email: ')
                if validate_email(email):
                    break

            print('\n-- Address\n')

            line1 = input('Line 1: ')
            line2 = input('Line 2: ')
            city = input('City: ')
            country = input('Country: ')

            while True:
                postcode = input('Postcode: ')
                if validate_postcode(postcode):
                    break

            address = Address(line1, line2, city, country, postcode)
            contact = Contact((None if operation == 'create' else old_contact.id), fname, sname, phone, email, address, False)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{contact}')
            if input('\nAre you happy with the details entered? (y/n) ➡ ').lower() == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')
                Contact.last_id += 1
                return contact
