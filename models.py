from sqlalchemy import Column, Date, ForeignKey, Integer, Text
from sqlalchemy.dialects.mysql import TINYINT, TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import Model

Base = declarative_base()
metadata = Base.metadata


class Genre(Model):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, unique=True)
    Name = Column(Text)
    Description = Column(Text)


class Position(Model):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True, unique=True)
    PositionName = Column(Text)
    Salary = Column(Integer)
    Duties = Column(Text)
    Requirements = Column(Text)


class Publisher(Model):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True, unique=True)
    Publisher_Name = Column(Text)
    City = Column(Text)
    Adress = Column(Text)


class Reader(Model):
    __tablename__ = 'reader'

    id = Column(Integer, primary_key=True, unique=True)
    Name = Column(Text)
    Surname = Column(Text)
    Fathers_Name = Column(Text)
    Date_Of_Birth = Column(Date)
    Sex = Column(TINYTEXT)
    Adress = Column(Text)
    Phone_number = Column(TINYTEXT)
    PassportID = Column(TINYTEXT)


class Book(Model):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, unique=True)
    Name = Column(Text)
    Author = Column(Text)
    Publisher_id = Column(Integer, ForeignKey('publisher.id'))
    publisher = relationship("Publisher")
    Year_Of_Issue = Column(Date)
    Genre_ID = Column(Integer, ForeignKey('genre.id'))

    Genre = relationship("Genre")
    Publisher = relationship('Publisher')


class Worker(Model):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True, unique=True)
    Name = Column(Text)
    Surname = Column(Text)
    Fathers_Name = Column(Text)
    Age = Column(Integer)
    Sex = Column(TINYTEXT)
    Adress = Column(Text)
    PassportID = Column(TINYTEXT)
    PossitionID = Column(ForeignKey('position.id'), index=True)

    position = relationship('Position')


class IssuedBook(Model):
    __tablename__ = 'issued_book'

    id = Column(Integer, primary_key=True, unique=True)
    book_id = Column(ForeignKey('book.id'), index=True)
    reader_id = Column(ForeignKey('reader.id'), index=True)
    date_of_issue = Column(Date)
    return_date = Column(Date)
    return_mark = Column(TINYINT(1))
    worker_id = Column(ForeignKey('worker.id'), index=True)

    book = relationship('Book')
    reader = relationship('Reader')
    worker = relationship('Worker')
