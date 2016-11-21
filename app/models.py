from app import db
from sqlalchemy.sql import func

class RiverStation(db.Model):
  __tablename__ = 'RiverStation'
  riverstation_id = db.Column(db.Integer, primary_key=True, nullable=False)
  riverstation_uid = db.Column(db.String(64), unique=True, index=True, nullable=False)
  location_code = db.Column(db.Integer, unique=True, index=True)
  osgr_easting = db.Column(db.Integer, nullable=False)
  osgr_northing = db.Column(db.Integer, nullable=False)
  latitude = db.Column(db.Float, nullable=False)
  longitide = db.Column(db.Float, nullable=False)
  measurments = db.relationship('Measurment', backref='station')

  def __repr__(self):
    return '<Station id:%d, name:%r' % (self.riverstation_id, self.riverstation_uid)

class RiverLevel(db.Model):
  __tablename__= 'RiverLevel'
  riverlevel_id = db.Column(db.Integer, primary_key=True, nullable=False)
  riverstation_id = db.Column(db.Integer, db.ForeignKey('stations.id'), nullable=False)
  sampled_at = db.Column(db.DateTime, nullable=False)
  archived_at = db.Column(db.DateTime, default=func.now(), nullable=False)
  level = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return '<Measurment id:%d, date:%c, value:%0.3f' % (self.id, self.date_time, self.value)
