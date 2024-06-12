from data import Controller
from utils import validate_id
from argparse import ArgumentParser

def main():
    controller = Controller('./data/contacts.db')

    parser = ArgumentParser()

    group = parser.add_mutually_exclusive_group()

    group.add_argument('--all', '-a', action='store_true', help='View all contacts in your contact book')
    group.add_argument('--get', '-g', help='Get a specific contact by ID')
    group.add_argument('--new', '-n', action='store_true', help='Create a new contact')
    group.add_argument('--update', '-u', help='Update a specific contact by ID')
    group.add_argument('--delete', '-d', help='Delete a specific contact by ID')

    args = parser.parse_args()

    if args.all:
        controller.get_all_contacts()

    if args.get:
        if validate_id(args.get):
            controller.get_contact(args.get)

    if args.new:
        controller.new_contact()

    if args.update:
        if validate_id(args.update):
            controller.update_contact(args.update)

    if args.delete:
        if validate_id(args.delete):
            controller.delete_contact(args.delete)





if __name__ == '__main__':
    main()