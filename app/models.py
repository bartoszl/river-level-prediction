from app import db
from sqlalchemy.sql import func

class RiverStation(db.Model):
  __tablename__ = 'RiverStation'
  riverstation_id = db.Column(db.Integer, primary_key=True, nullable=False)
  riverstation_uid = db.Column(db.String(64), unique=True, index=True, nullable=False)
  osgr_easting = db.Column(db.Integer, nullable=False)
  osgr_northing = db.Column(db.Integer, nullable=False)
  latitude = db.Column(db.Float, nullable=False)
  longitide = db.Column(db.Float, nullable=False)
  river_level = db.relationship('RiverLevel', backref='RiverStation')

  def __repr__(self):
    return '<Station id:%d, name:%r' % (self.riverstation_id, self.riverstation_uid)

class RiverLevel(db.Model):
  __tablename__= 'RiverLevel'
  riverlevel_id = db.Column(db.Integer, primary_key=True, nullable=False)
  riverstation_id = db.Column(db.Integer, db.ForeignKey('RiverStation.riverstation_id'), nullable=False)
  sampled_at = db.Column(db.DateTime, nullable=False)
  archived_at = db.Column(db.DateTime, default=func.now(), nullable=False)
  level = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return '<Measurment id:%d, date:%c, value:%0.3f' % (self._riverlevel_id, self.sampled_at, self.level)

class WeatherStation(db.Model):
    __tablename__= 'WeatherStation'
    weatherstation_id = db.Column(db.Integer, primary_key=True, nullable=False)
    weatherstation_uid = db.Column(db.String(64), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class CurrentWeather(db.Model):
    __tablename__= 'CurrentWeather'
    currentweather_id = db.Column(db.Integer, primary_key=True, nullable=False)
    weatherstation_id = db.Column(db.Integer, db.ForeignKey('WeatherStation.weatherstation_id'), nullable=False)
    archived_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    sampled_at = db.Column(db.DateTime, nullable=False)
    precipation = db.Column(db.Float, nullable=False)
