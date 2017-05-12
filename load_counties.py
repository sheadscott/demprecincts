#!flask/bin/python

from app import db, models

f = open('../vogb/GIS/db/us-counties.csv', 'r')

for line in f:
    county = line.rstrip().split(',')
    state = models.State.query.filter_by(name=county[1].upper()).first()
    s_id = state.id
    # print(county[1], s_id)
    c = models.County(name=county[0], state=s_id)
    db.session.add(c)
    
db.session.commit()
