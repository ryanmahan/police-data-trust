from .. import db
from .types.enums import Gender
from .types.enums import Race
import enum


class Rank(str, enum.Enum):
    # TODO: Is this comprehensive?
    TECHNICIAN = "TECHNICIAN"
    OFFICER = "OFFICER"
    DETECTIVE = "DETECTIVE"
    CORPORAL = "CORPORAL"
    SERGEANT = "SERGEANT"
    LIEUTENANT = "LIEUTENANT"
    CAPTAIN = "CAPTAIN"
    DEPUTY = "DEPUTY"
    CHIEF = "CHIEF"


<<<<<<< HEAD
class Officer(db.model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO: Is this different than primary key, can we name it better
    officer_ID = db.Column(db.String)
    first = db.Column(db.String)
    last = db.Column(db.String)
    gender = db.Column(db.String)
    race = db.Column(db.String)
    apptDate = db.Column(db.DateTime)
    # TODO: is this a number?
    unit = db.Column(db.String)
    rank = db.Column(db.Enum(Rank))
    # TODO: number of stars?
    star = db.Column(db.Integer)
    age = db.Column(db.Integer)
=======
class Officer(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # officer id
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    race = db.Column(db.Enum(Race))
    gender = db.Column(db.Enum(Gender))
    appointed_date = db.Column(db.DateTime)
    badge = db.Column(db.Text)
    unit = db.Column(db.Text)  # type?
    # Note: rank at time of incident
    rank = db.Column(db.Text)  # type?
    star = db.Column(db.Text)  # type?
    date_of_birth = db.Column(db.Date)
    # TODO: Age changes over time. Might we use birth year?


class OfficerAtIncident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO: Relationships, fields?
>>>>>>> 682aa264d7fbb0a7bdf4530e2623a07c69f3b07f
