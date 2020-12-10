from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from models import Book, Publisher, Reader, Worker, Genre, Position, IssuedBook;


class BookModelView(ModelView):
    datamodel = SQLAInterface(Book)

    label_columns = {'Name': 'Name of book', 'Genre.Name': 'Genre', 'Publisher.Publisher_Name': 'Publisher'}
    list_columns = ['Name', 'Author', 'Year_Of_Issue', 'Genre.Name', 'Publisher.Publisher_Name']




class HRModelView(ModelView):
    datamodel = SQLAInterface(Book)

    label_columns = {'Name': 'Name of book', 'Genre.Name': 'Genre', 'Publisher.Publisher_Name': 'Publisher'}
    list_columns = ['Name', 'Author', 'Year_Of_Issue', 'Genre.Name', 'Publisher.Publisher_Name']



class PublisherModelView(ModelView):
    datamodel = SQLAInterface(Publisher)

    list_columns = ['Publisher_Name', 'City', 'Adress']


class HRModelView(ModelView):
    datamodel = SQLAInterface(Worker)
    can_add = False
    can_edit = False

    list_columns = ['Name','Surname','Fathers_Name', 'Age', 'Sex','Adress','position.PositionName']



class Catalog(ModelView):
    datamodel = SQLAInterface(Book)
    can_add = False
    can_edit = False

    list_columns = ['Name','Author','Year_Of_Issue', 'Genre.Name', 'publisher.Publisher_Name', 'publisher.City']



class Books_On_HandsView(ModelView):
    datamodel = SQLAInterface(IssuedBook)

    list_columns = ['book.Name','book.Author','reader.Name', 'reader.id', 'date_of_issue', 'return_mark', 'worker.Name', 'worker.Surname']



class ReaderModelView(ModelView):
    datamodel = SQLAInterface(Reader)

    list_columns = ['Name', 'Surname', 'Fathers_Name', 'Date_Of_Birth', 'Sex', 'Adress', 'Phone_number', 'PassportID']




class WorkerModelView(ModelView):
    datamodel = SQLAInterface(Worker)

    list_columns = ['id', 'Name', 'Surname', 'Fathers_Name', 'Age', 'Sex', 'Adress', 'PassportID',
                    'position.PositionName']




class PositionModelView(ModelView):
    datamodel = SQLAInterface(Position)

    list_columns = ['id', 'PositionName', 'Salary', 'Duties', 'Requirements']




class IssuedBookModelView(ModelView):
    datamodel = SQLAInterface(IssuedBook)

    list_columns = ['id', 'book.Name', 'reader.Name', 'date_of_issue', 'return_date', 'return_mark', 'worker.Name']



class GenreModelView(ModelView):
    datamodel = SQLAInterface(Genre)

    list_columns = ['id', 'Name', 'Description']


