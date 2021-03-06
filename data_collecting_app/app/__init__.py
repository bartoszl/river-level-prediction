from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_apscheduler import APScheduler
import logging

logging.basicConfig()

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)

db = SQLAlchemy(app)

from app import views, models, jobs

migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app,
                db=db,
                RiverStation=models.RiverStation,
                RiverLevel=models.RiverLevel,
                WeatherStation=models.WeatherStation,
                CurrentWeather=models.CurrentWeather)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
