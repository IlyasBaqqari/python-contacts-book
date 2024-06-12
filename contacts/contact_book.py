from dataclasses import dataclass, field
from .contact import Contact

# Class is only used if using objects and not DB

@dataclass
class ContactBook:
    contacts: [Contact] = field(default_factory=list)

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)