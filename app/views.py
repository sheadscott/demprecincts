from flask import render_template, flash, redirect
from app import app, db
from datetime import datetime
from .forms import ContactForm
from .models import User, State

app.jinja_env.line_statement_prefix = '#'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    contact = ContactForm()
    state_list = [(s.postal_code, s.name) for s in State.query.order_by('postal_code')]
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
        if userEmail != None:
            pass # Send an email of the message instead of creating a new userEmail
        else:
            db.session.add(u)
            db.session.commit()
            flash('Thanks %s! We will let you as we roll out more features' %
                str(contact.first_name.data))
                
        return redirect('/index/')
    return render_template('contact.html.j2',
                            contact=contact)


# Store Google Sheet URL in db
# Store center lat and long in db. Can get them by requesting a google search for the location
# Coordinates are stored in this: <div class="_XWk">32.7767° N, 96.7970° W</div>
# Pass these in to map()


@app.route('/map/')
@app.route('/map/<state>/<county>/')
def map(state=None, county=None):
    sheet = 'https://docs.google.com/spreadsheets/d/156SJVhA1jHg8kxGjBQfGRsdO3qVFry-rkX1jHo3AAV4/pubhtml'
    return render_template('map.html.j2', state=state, county=county, sheet=sheet)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html.j2'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html.j2'), 500
