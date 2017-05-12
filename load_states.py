#!flask/bin/python

from app import db, models

f = open('../vogb/GIS/db/state-postal-codes.csv', 'r')

for line in f:
    state = line.rstrip().split(',')
    s = models.State(name=state[0], postal_code=state[1])
    db.session.add(s)

db.session.commit()

models.State.query.all()
