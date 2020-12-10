from flask import Flask
from .config import Config
from views import *
from index import MyIndexView
from flask_sqlalchemy import SQLAlchemy
from flask_appbuilder import  AppBuilder
#from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, )

db.create_all()
appbuilder.add_view(
    BookModelView,
    "List Books",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    PublisherModelView,
    "List Publisher",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    HRModelView,
    "HRDepartment",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    ReaderModelView,
    "List Readers",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    Catalog,
    "Catalog",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    Books_On_HandsView,
    "Books on_hands",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    WorkerModelView,
    "List Worker",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)

appbuilder.add_view(
    PositionModelView,
    "List Position",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)

appbuilder.add_view(
    IssuedBookModelView,
    "List Issued books",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    GenreModelView,
    "List Genres",
    icon = "fa-folder-open-o",
    category = "Library",
    category_icon = "fa-envelope"
)

app.run(debug=True)