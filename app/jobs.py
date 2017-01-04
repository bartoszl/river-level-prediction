import requests
import csv
from app import app, db
from app.models import RiverStation, RiverLevel, WeatherStation, CurrentWeather
import os
from grid_to_ne import get_ne_lat_long
import datetime

def test():
    print 'test'

def pull_river_level_data(urls):
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        for url in urls:
            r = requests.get(url)
            if r.status_code != 404:
                l = csv_to_list(r)
                data_index = get_measurment_index(l) + 1
                station_id = get_or_create_station(l)
                for m in l[data_index:]:
                    if m:
                        add_measurment(m, station_id)
                        db.session.commit()
                print "Fetched River Level for :" + str(station_id)
            else:
                print "404 Something is wrong with the url: " + url


def add_measurment(m, station_id):
    sampled_at = datetime.datetime.strptime(m[0], '%d/%m/%Y %H:%M:%S')
    riverlevel = RiverLevel.query.filter_by(
        riverstation_id=station_id,
        sampled_at=sampled_at).first()
    if len(m) == 2 and  riverlevel== None:
        meas = RiverLevel()
        meas.riverstation_id = station_id
        meas.sampled_at = datetime.datetime.strptime(m[0], '%d/%m/%Y %H:%M:%S')
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
    station_name = get_station_name(result)
    station = RiverStation.query.filter_by(riverstation_uid=station_name).first()
    if station == None:
        station = RiverStation()
        station.riverstation_uid = station_name
        e,n,lon,lat = get_coords(station_name)
        station.osgr_easting = e;
        station.osgr_northing = n;
        station.longitide = lon;
        station.latitude = lat;
        db.session.add(station)
        db.session.commit()
    return station.riverstation_id

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
        if row and station_name == row[name_i]:
            return get_ne_lat_long(row[ngr_i])

def station_name_index(row):
    for index, field in enumerate(row):
        if(field=="STATION_NAME"):
            return index

def ngr_index(row):
    for index, field in enumerate(row):
        if(field=="NATIONAL_GRID_REFERENCE"):
            return index


####### WEATHER JOB ########

def get_weather():
    api_key = "32f94d7321018228f4a37b517df35858"
    url = "http://api.openweathermap.org/data/2.5/weather?q=Glasgow,uk&appid=" + api_key
    r = requests.get(url)
    weather = r.json()
    weather_station_id = get_or_create_weather_station(weather)
    current_weather = CurrentWeather()
    current_weather.weatherstation_id = weather_station_id
    current_weather.precipation = weather['rain']['3h'] if 'rain' in weather else 0
    current_weather.temperature = weather['main']['temp']
    current_weather.wind_speed = weather['wind']['speed']
    current_weather.wind_direction = weather['wind']['deg']
    current_weather.description = weather['weather'][0]['description']
    current_weather.sampled_at = datetime.datetime.fromtimestamp(
                                        int(weather['dt'])
                                    ).strftime('%d/%m/%Y %H:%M:%S')
    db.session.add(current_weather)
    db.session.commit()
    print 'Weather fetched ' + str(current_weather.sampled_at)

def get_or_create_weather_station(weather):
    weather_station = WeatherStation.query.filter_by(weatherstation_uid=weather['name']).first()
    if not weather_station:
        weather_station = WeatherStation()
        weather_station.weatherstation_uid = weather['name']
        weather_station.longitude = weather['coord']['lon']
        weather_station.latitude = weather['coord']['lat']
        db.session.add(weather_station)
        db.session.commit()
    return weather_station.weatherstation_id
