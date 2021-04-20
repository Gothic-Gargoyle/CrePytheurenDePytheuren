# TODO: add database for persistent storage
import sqlite3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy import Date, DATETIME, Boolean, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Connect to DB, otherwise create
engine = create_engine('sqlite://test.db', echo=True)

Base = declarative_base()

# Koppeltabellen
administration_ledger = Table(
    "administration_ledger", Base.metadata,
    Column("administration_id", Integer, ForeignKey="administration.administration_id"),
    Column("ledger_id", Integer, ForeignKey="ledger.ledger_id")
)

ledgers_entry = Table(
    "ledgers_entry", Base.metadata,
    Column("ledger_id", Integer, ForeignKey="ledger.ledger_id"),
    Column("entry_id", Integer, ForeignKey="journal_entry.entry_id")
)

ledger_relations = Table(
    "ledger_relations", Base.metadata,
    Column("ledger_id", Integer, ForeignKey="ledger.ledger_id"),
    Column("relation_id", Integer, ForeignKey="relation.relation_id")
)



# tables!
class administration(Base):
    __tablename__ = "administration"
    administration_id = Column('administration_id', Integer, primary_key=True),
    administration_name = Column(String)
    ledgers = relationship()


class ledger(Base):
    __tablename__ = "ledger"
    ledger_id = Column(Integer, primary_key=True),
    ledger_name = Column(String),
    relations = relationship()


class journal_entry(Base):
    __tablename__ = "journal_entry"
    journal_id = Column(Integer, primary_key=True),
    bookdate = Column(Date),
    amount = Column(Integer),
    cod = Column(Boolean),
    vat = Column(Integer),
    description = Column(String)


class relation(Base):
    __tablename__ = "relation"
    relation_id = Column(Integer, primary_key=True),
    relation_name = Column(String),
    relation_iban = Column(String)

