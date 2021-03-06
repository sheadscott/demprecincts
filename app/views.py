from flask import render_template, flash, redirect, request
from app import app, db
from datetime import datetime
from .forms import ContactForm
from .models import User, State, County
from .emails import send_contact_notification

app.jinja_env.line_statement_prefix = '#'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():

    contact = ContactForm()
    state_list = [(s.postal_code, s.name.title()) for s in State.query.order_by('postal_code')]
    state_list.insert(0, ('', '-- State --'))
    contact.state.choices = state_list
    if contact.validate_on_submit():
        u = User(first_name=contact.first_name.data,
                    last_name=contact.last_name.data,
                    email=contact.email.data,
                    state=contact.state.data,
                    county=contact.county.data,
                    position=contact.position.data,
                    timestamp=datetime.utcnow())

        userEmail = User.query.filter_by(email=u.email).first()
        msg = contact.message.data
        send_contact_notification(u, msg)
        flash('Thanks for your interest!<br><br>We will be in contact with you at:<br>{0}'.format(contact.email.data))

        if userEmail != None:
            pass
        else:
            db.session.add(u)
            db.session.commit()


        return redirect('/')

    else:
        pass
        # flash('There was a technical problem submitting your request. Please email us at demprecincts@mail.com<br>Errors: {0}'.format(contact.errors))

    return render_template('contact.html.j2',
                            contact=contact)


# Store Google Sheet URL in db
# Store center lat and long in db. Can get them by requesting a google search for the location
# Coordinates are stored in this: <div class="_XWk">32.7767° N, 96.7970° W</div>
# Pass these in to map()


@app.route('/map/<state>/<county>/')
def map(state=None, county=None):
    state = state.upper()
    if county == 'mclennan':
        county = 'McLennan'
    else:
        county = county.title()
    state_db = State.query.filter_by(postal_code=state).first()
    county_db = state_db.counties.filter(County.name==county).first()
    sheet = county_db.sheet_url
    geojson = county_db.geojson_url
    latitude = county_db.latitude
    longitude = county_db.longitude

    return render_template('map.html.j2', state=state, county=county, sheet=sheet, geojson=geojson, latitude=latitude, longitude=longitude)

@app.route('/tx-house-2018/')
def txhouse():
    latitude = 31.9686
    longitude = 99.9018

    return render_template('tx-house-2018.html.j2', latitude=latitude, longitude=longitude)

@app.route('/tx-house-2020/')
def txhouse2020():
    latitude = 31.9686
    longitude = 99.9018

    return render_template('tx-house-2020.html.j2', latitude=latitude, longitude=longitude)

@app.route('/tx-senate-2018/')
def txsenate():
    latitude = 31.9686
    longitude = 99.9018

    return render_template('tx-senate-2018.html.j2', latitude=latitude, longitude=longitude)

@app.route('/election/<state>/<county>/')
def election(state=None, county=None):
    state = state.upper()
    if county == 'mclennan':
        county = 'McLennan'
    else:
        county = county.title()
    state_db = State.query.filter_by(postal_code=state).first()
    county_db = state_db.counties.filter(County.name==county).first()
    # sheet = county_db.sheet_url
    sheet = 'https://docs.google.com/spreadsheets/d/1zeKExlxt5kd5YnJgJrLtGb6FpzgGzSXKPlk1oJqw41U/pub?output=csv' # Travis County Election Judges
    geojson = county_db.geojson_url
    latitude = county_db.latitude
    longitude = county_db.longitude

    return render_template('election-map.html.j2', state=state, county=county, sheet=sheet, geojson=geojson, latitude=latitude, longitude=longitude)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html.j2'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html.j2'), 500
