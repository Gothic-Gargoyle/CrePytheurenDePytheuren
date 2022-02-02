import sqlalchemy as db
import models
bookkeeping = db.create_engine('sqlite:///bookkeeping.db', echo=True)
connection = bookkeeping.connect()
def create_db():
    ...

def connect_db():
    bookkeeping.connect()
    print("Connected to DB!")

# CREATE
def add_administration():
    ...

def add_account(id, name, hasrel):
    newAccount = models.account(account_id = id,
                                account_name = name,
                                has_relations = hasrel)


def add_relation():
    ...

def add_journal_entry():
    ...


#READ



# UPDATE
def update_administration():
    ...

def update_ledger():
    ...

def update_relation():
    ...

def update_journal_entry():
    ...

# DELETE
def remove_journal_entry():
    ...