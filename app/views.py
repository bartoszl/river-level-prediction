from app import app, db
from jobs import pull_river_level_data

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
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
      'http://apps.sepa.org.uk/database/riverlevels/133066-SG.csv'
    ]
    pull_river_level_data(SEPA_RIVER_LEVEL_URLS)
    return 'done'
