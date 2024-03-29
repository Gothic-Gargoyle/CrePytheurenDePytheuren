# Models for DB
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy import Date, DATETIME, Boolean, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.declarative import declarative_base
# sqlite, want luiheid.
engine = create_engine('sqlite:///bookkeeping.db', echo=True)

meta = MetaData()

# normale tabellen
administration = Table(
    'administration', meta,
    Column('administration_id', Integer, primary_key=True),
    Column("administration_name", String),
)

account = Table(
    "account",meta,
    Column('account_id', Integer, primary_key=True),
    Column('account_name',String),
    Column('has_relations', Boolean),
)


journal_entry = Table(
    "journal_entry", meta,
    Column('journal_entry_id', Integer, primary_key=True),
    Column('bookdate', Date),
    Column('period', Integer),
    Column('amount', Integer),
    Column('cod', Boolean),
    Column('vat', Integer),
    Column('description', String),
    Column('definitive', Boolean),
)

relation = Table(
    "relation", meta,
    Column('relation_id',Integer, primary_key=True),
    Column('relation_name', String),
    Column('relation_iban', String),
)

# Koppeltabellen
administration_ledger = Table(
    "administration_ledger", meta,
    Column("administration_id", Integer, ForeignKey('administration.administration_id')),
    Column("account_id", Integer, ForeignKey('account.account_id'))
)

account_entry = Table(
    "account_entry", meta,
    Column("account_id", Integer, ForeignKey('account.account_id')),
    Column("entry_id", Integer, ForeignKey('journal_entry.journal_entry_id'))
)

account_relations = Table(
    "account_relations", meta,
    Column("account_id", Integer, ForeignKey('account.account_id')),
    Column("relation_id", Integer, ForeignKey('relation.relation_id'))
)

meta.create_all(engine)