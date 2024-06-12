from typing import List, Tuple, Union
import sqlite3, sys

sys.path.append('..')
from contacts import Contact, Address
class DatabaseManager:
    def __init__(self, db_url: str) -> None:
        self.db_url = db_url

    def create_connection(self) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        connection = sqlite3.connect(self.db_url)
        cursor = connection.cursor()
        return connection, cursor


    def init_table(self) -> None:
        connection, cursor = self.create_connection()

        create_query = '''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER not null primary key unique,
                'firstname(s)' TEXT,
                'surname(s)'   TEXT,
                phone          TEXT,
                email          TEXT,
                address_line_1 TEXT,
                address_line_2 TEXT,
                city           TEXT,
                country        TEXT,
                postcode       TEXT
            );
        '''
        cursor.execute(create_query)
        connection.commit()

        cursor.close()
        connection.close()


    def get_all_contacts(self) -> List[Contact]:
        connection, cursor = self.create_connection()

        select_query = 'SELECT * FROM contacts;'
        cursor.execute(select_query)
        data = cursor.fetchall()

        contacts = []
        for contact in data:
            address = Address(contact[5], contact[6], contact[7], contact[8], contact[9])
            contacts.append(Contact(contact[0], contact[1], contact[2], contact[3], contact[4], address))
        return contacts


    def get_contact_by_id(self, id: str) -> Union[Contact, None]:
        connection, cursor = self.create_connection()

        select_query = f'SELECT * FROM contacts WHERE id = {id};'
        cursor.execute(select_query)
        contact = cursor.fetchone()

        if contact:
            address = Address(contact[5], contact[6], contact[7], contact[8], contact[9])
            return Contact(contact[0], contact[1], contact[2], contact[3], contact[4], address)

        return None


    def insert_contact(self, contact: Contact) -> None:
        connection, cursor = self.create_connection()

        insert_query = f'''
            INSERT INTO contacts
            VALUES (
                {contact.id}, 
                '{contact.first_name}', 
                '{contact.surname}', 
                '{contact.phone_number}', 
                '{contact.email}', 
                '{contact.address.line1}', 
                '{contact.address.line2}', 
                '{contact.address.city}', 
                '{contact.address.country}', 
                '{contact.address.postcode}'
            );
        '''
        cursor.execute(insert_query)
        connection.commit()

        cursor.close()
        connection.close()


    def update_contact(self, contact: Contact) -> None:
        connection, cursor = self.create_connection()

        update_query = f'''
            UPDATE contacts SET 
                'firstname(s)' = '{contact.first_name}', 
                'surname(s)' = '{contact.surname}',
                phone = '{contact.phone_number}',
                email = '{contact.email}',
                address_line_1 = '{contact.address.line1}',
                address_line_2 = '{contact.address.line2}',
                city = '{contact.address.city}',
                country = '{contact.address.country}',
                postcode =  '{contact.address.postcode}'
            WHERE id = {contact.id};
        '''
        cursor.execute(update_query)
        connection.commit()

        cursor.close()
        connection.close()


    def delete_contact(self, id: str) -> None:
        connection, cursor = self.create_connection()

        delete_query = f'DELETE FROM contacts WHERE id = {id};'
        cursor.execute(delete_query)
        connection.commit()

        cursor.close()
        connection.close()







