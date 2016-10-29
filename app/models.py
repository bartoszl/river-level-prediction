from app import db

class Station(db.Model):
  __tablename__ = 'stations'
  id = db.Column(db.Integer, primary_key=True)
  office = db.Column(db.String(64), unique=True)
  station_name = db.Column(db.String(64), unique=True, index=True)
  location_code = db.Column(db.Integer, unique=True, index=True)
  measurments = db.relationship('Measurment', backref='station')

  def __repr__(self):
    return '<Station id:%d, name:%r' % (self.id, self.station_name)

class Measurment(db.Model):
  __tablename__= 'measurments'
  id = db.Column(db.Integer, primary_key=True)
  station_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
  date_time = db.Column(db.DateTime)
  value = db.Column(db.Float)  

  def __repr__(self):
    return '<Measurment id:%d, date:%c, value:%0.3f' % (self.id, self.date_time, self.value)


