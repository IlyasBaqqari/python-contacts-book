# Python Contacts Book

**Ilyas Baqqari ~ 12.06.2024**

---

This app serves as a contacts book accessible through the command line, using 
several arguments to perform operations on an SQLite database.

## How to Use

Navigate to the directory containing `main.py` in your terminal, then run it 
using Python 3 like so:

```shell
python3 main.py <argument>
```

### Arguments

| Argument                   | Effect                                                       |
|----------------------------|--------------------------------------------------------------|
| `--all`, `-a`              | Displays all contacts present in the database                |
| `--get <id>`, `-g <id>`    | Displays a contact associated with a given ID                |
| `--new`, `-n`              | Creates a new contact in the database                        |
| `--update <id>`, `-u <id>` | Updates a contact in the database associated with a given ID |
| `--delete <id>`, `-u <id>` | Deletes a contact in the database associated with a given ID |