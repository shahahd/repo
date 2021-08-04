from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website= db.Column(db.String(120))
    seeking_talent=db.Column(db.Boolean)
    seeking_description=db.Column(db.String)
    

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website= db.Column(db.String(120))
    seeking_venues=db.Column(db.Boolean)
    seeking_description=db.Column(db.String)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
class Show(db.Model):
  __tablename__="shows"
  
  id=db.Column(db.Integer,primary_key=True)
  venue_id=db.Column(db.Integer,db.ForeignKey('venue.id'),nullable=False)
  artist_id=db.Column(db.Integer,db.ForeignKey('artist.id'),nullable=False)
  show_date=db.Column(db.DateTime,nullable=False)
  
  # relationships
  Venue_r=db.relationship('Venue',backref=db.backref('shows', cascade='all, delete'))
  artist_r=db.relationship('Artist',backref=db.backref('shows', cascade='all, delete'))
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.