# TODO: add database for persistent storage
#
import sqlite3
from sqlalchemy import create_engine, MetaData, PrimaryKeyConstraint, Table, Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy import Date, DATETIME, Boolean, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Connect to DB, otherwise create
engine = create_engine('sqlite:///bookkeeping.db', echo=True)

Base = declarative_base()

# Koppeltabellen
class administration_account(Base):
    __tablename__ = 'administration_account'
    administration_id = Column("administration_id", Integer, ForeignKey('administration.administration_id'))
    account_id = Column("account_id", Integer, ForeignKey('account.account_id'))

class account_entry(Base):
    __tablename__ = 'account_entry'
    __table_args__ = (PrimaryKeyConstraint('account.account_id','journal_entry.entry_id'),)
    account_id = Column("account_id", Integer, ForeignKey('account.account_id'))
    entry_id = Column("entry_id", Integer, ForeignKey('journal_entry.entry_id'))

class ledger_relations(Base):
    __tablename__ = 'account_relations'
    __table_args__ = (PrimaryKeyConstraint('account.account_id', 'relation.relation_id'),)
    account_id = Column('account_id', Integer, ForeignKey('account.account_id'))
    relation_id = Column('relation_id', Integer, ForeignKey('relation.relation_id'))



# tables!
class administration(Base):
    __tablename__ = "administration"
    administration_id = Column('administration_id', Integer, primary_key=True)
    administration_name = Column(String)
    accounts = relationship()


class account(Base):
    __tablename__ = "account"
    account_id = Column(Integer, primary_key=True)
    account_name = Column(String)
    relations = relationship()


class journal_entry(Base):
    __tablename__ = "journal_entry"
    journal_entry_id = Column(Integer, primary_key=True)
    bookdate = Column(Date)
    amount = Column(Integer)
    cod = Column(Boolean)
    vat = Column(Integer)
    description = Column(String)


class relation(Base):
    __tablename__ = "relation"
    relation_id = Column(Integer, primary_key=True)
    relation_name = Column(String)
    relation_iban = Column(String)

