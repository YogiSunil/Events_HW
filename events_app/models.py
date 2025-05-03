"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from sqlalchemy import Enum
import enum

class EventType(enum.Enum):
    PARTY = "Party"
    STUDY = "Study"
    NETWORKING = "Networking"

# Define the association table for the many-to-many relationship between Event and Guest
guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'))
)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    events_attending = db.relationship('Event', secondary=guest_event_table, back_populates='guests')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    event_type = db.Column(Enum(EventType), nullable=True)
    guests = db.relationship('Guest', secondary=guest_event_table, back_populates='events_attending')