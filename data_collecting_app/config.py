import os

SQLALCHEMY_DATABASE_URI = 'postgresql:///bartosz'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SEPA_RIVER_LEVEL_URLS = [
  'http://apps.sepa.org.uk/database/riverlevels/133099-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133138-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133074-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133093-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133118-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133061-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133080-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133119-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133113-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133114-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/504722-SG.csv',
  'http://apps.sepa.org.uk/database/riverlevels/133182-SG.csv'
]

CITIES = [ 'Glasgow,uk', 'Moffat,uk']

JOBS = [
  {
    'id': 'river_level',
    'func': 'app.jobs:pull_river_level_data',
    'args': [SEPA_RIVER_LEVEL_URLS],
    'trigger': 'interval',
    'hours': 12
  },
  {
    'id': 'current_weahter',
    'func': 'app.jobs:get_weather',
    'args': [CITIES],
    'trigger': 'interval',
    'minutes': 15
  }
]

WEATHER_API_KEY = "32f94d7321018228f4a37b517df35858"
