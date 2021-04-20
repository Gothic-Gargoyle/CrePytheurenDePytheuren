# Models for DB
from sqlalchemy import Column, Integer, String, ForeignKey, Table

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base
# sqlite, want luiheid.

base = declarative_base()
