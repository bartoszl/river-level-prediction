import requests
import csv
from app import app, db
from app.models import RiverStation, RiverLevel
import os
from grid_to_ne import get_ne_lat_long

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
    meas.riverstation_id = station_id
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
    station.riverstation_uid = get_station_name(result)
    e,n,lon,lat = get_coords(station.riverstation_uid)
    station.osgr_easting = e;
    station.osgr_northing = n;
    station.longitide = lon;
    station.latitude = lat;
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

def get_coords(station_name):
    url = 'http://apps.sepa.org.uk/database/riverlevels/SEPA_River_Levels_Web.csv'
    r = requests.get(url)
    l = csv_to_list(r)
    name_i = station_name_index(l[0])
    ngr_i = ngr_index(l[0])
    for row in l:
        if station_name == l[name_i]:
            return get_ne_lat_long(l[ngr_i])

def station_name_index(row):
    for index, field in enumerate(row):
        if(field=="STATION_NAME"):
            return index

def ngr_index(row):
    for index, field in enumerate(row):
        if(field=="NATIONAL_GRID_REFERENCE"):
            return index
