#!flask/bin/python

from app import db, models

name = 'Travis'
state_code = 'TX'
sheet_url = 'https://docs.google.com/spreadsheets/d/1W4vl0dxr2fkmiLSvMA9_y4m6YlVMZ9l0EuNPGEZHqDs/pubhtml'
geojson_url = 'https://cdn.rawgit.com/sheadscott/county-voting-precincts/a6a4aac8/tx/travis.geojson'
latitude = 30.267
longitude = 97.743


state = models.State.query.filter_by(postal_code=state_code).first()
s_id = state.id
county = models.County(name=name, state=s_id, sheet_url=sheet_url, geojson_url=geojson_url, latitude=latitude, longitude=longitude)
db.session.add(county)

db.session.commit()
