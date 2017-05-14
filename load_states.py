#!flask/bin/python

from app import db, models

f = open('./db_tools/state-postal-codes.csv', 'r')

for line in f:
    state = line.rstrip().split(',')
    s = models.State(name=state[0], postal_code=state[1])
    db.session.add(s)

db.session.commit()
