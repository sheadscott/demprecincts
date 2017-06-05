#!flask/bin/python

from app import db, models

name = 'Llano'
state_code = 'TX'
sheet_url = 'https://docs.google.com/spreadsheets/d/16L2OwGGQ3c4GrnO-IaNqTW1r0N1RWcuvfyc0pzeocbc/pub?output=csv'
latitude = 30.7593
longitude = 98.6750

state = models.State.query.filter_by(postal_code=state_code).first()
s_id = state.id

def add_county(s_id):
    county = models.County(name=name,
                           state=s_id,
                           sheet_url=sheet_url,
                           latitude=latitude,
                           longitude=longitude)
    db.session.add(county)

def update_county(s_id, county):
    county = models.County.query.filter_by(name=county).first()
    county.sheet_url = sheet_url
    # Add any columns that need to get updated here

#  update_county(s_id, 'Travis')

add_county(s_id)

db.session.commit()
