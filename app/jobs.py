import requests
import csv
from app import app, db
from app.models import RiverStation, RiverLevel
import os

def test(arg):
  if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    for url in arg:
      print url


def pull_river_level_data(urls):
  if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    for url in urls:
      r = requests.get(url)
      l = csv_to_list(r)

      data_index = get_measurment_index(l) + 1
      station_id = get_or_create_station(l)

      for m in l[data_index:]:
        add_measurment(m, station_id)

      db.session.commit()

      print 'done: '+url;


def add_measurment(m, station_id):
  if len(m) == 2 and RiverLevel.query.filter_by(riverstation_id=station_id, sampled_at=m[0]).first() == None:
    meas = RiverLevel()
    meas.rivverstation_id = station_id
    meas.sampled_at = m[0]
    meas.level = m[1]
    db.session.add(meas)


def csv_to_list(r):
  text = r.iter_lines()
  reader = csv.reader(text, delimiter=",")
  l = []
  for m in reader:
    l.append(m)
  return l

def get_measurment_index(result):
  for index, row in enumerate(result):
    if row[0] == 'Date/Time':
      return index

def get_or_create_station(result):

  location_code = get_location_code(result)

  station = RiverStation.query.filter_by(location_code=location_code).first()

  if station == None:
    station = RiverStation()
    #station.office = get_office(result)
    station.riverstation_uid = get_station_name(result)
    station.location_code = location_code
    db.session.add(station)
    db.session.commit()
  return station.id


def get_location_code(result):
  for row in result:
    if row[0] == 'Location Code':
      return row[1]

def get_office(result):
  for row in result:
    if row[0] == 'Office':
      return row[1]

def get_station_name(result):
  for row in result:
    if row[0] == 'Station Name':
      return row[1]
