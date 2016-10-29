from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)

db = SQLAlchemy(app)

from app import views, models

migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, Station=models.Station, Measurment=models.Measurment)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
