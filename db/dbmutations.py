from sqlalchemy import create_engine
import models
engine = create_engine('sqlite:///bookkeeping.db', echo=True)
def create_db():
    ...

def connect_db():
    engine.connect()
    print("Connected to DB!")

# CREATE
def add_administration():
    ...

def add_ledger():
    ...

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