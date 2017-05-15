from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    state = db.Column(db.Integer, db.ForeignKey('state.id'))
    county = db.Column(db.Integer, db.ForeignKey('county.id'))
    position = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r, %r>' % (self.first_name, self.email)


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    postal_code = db.Column(db.String(64))
    counties = db.relationship('County', backref='stateid', lazy='dynamic')

    def __repr__(self):
        return '<State %r>' % (self.name)


class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.Integer, db.ForeignKey('state.id'))
    sheet_url = db.Column(db.String(128))
    geojson_url = db.Column(db.String(128))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return '<County %r>' % (self.name)
