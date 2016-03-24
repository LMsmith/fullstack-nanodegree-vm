import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'Category'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    items = relationship('Item', cascade="all,delete-orphan", backref="category")

class Item(Base):
    __tablename__ = 'Item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8), nullable = False)
    image = Column(String)
    category_id = Column(Integer, ForeignKey('Category.id'))

####### end of file #######
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)