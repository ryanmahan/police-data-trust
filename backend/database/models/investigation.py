from .. import db
import enum


class Finding(str, enum.Enum):
    # TODO: Enum values
    flake = "NEEDS AN INDENTED LINE"


class Investigation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    official_id = db.Column(db.Integer)
    investigator_name = db.Column(db.String)
<<<<<<< HEAD
    investigator_name = db.Column(db.String)
=======
>>>>>>> 682aa264d7fbb0a7bdf4530e2623a07c69f3b07f
    investigator_rank = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    finding = db.Column(
        db.Enum(Finding)
<<<<<<< HEAD
    )  # Did this happen? Exoneration? (Status or invstigation result; enum with standardized options)
    # recomendation: # Might be useful to differentiate invstigator outcome and final outcome
    # TODO: Also an enum?
    outcome = db.Column(
        db.String
    )  # Outcomes may change based on the insitution; Can be overriden downstream,
    # Reason for Outcome?
    # TODO: also an enum?
    allegation = db.Column(db.String)
    # TODO: What does an allegation code look like? Should we have a mapper from int/str to user-facing language?
=======
    )  # Did this happen? Exoneration? (Status or invstigation result; enum
    # with standardized options)
    # recomendation: Might be useful to differentiate invstigator outcome and
    # final outcome
    # TODO: Also an enum?
    outcome = db.Column(
        db.String
    )  # Outcomes may change based on the insitution;
    # Can be overriden downstream.
    # Reason for Outcome?
    # TODO: also an enum?
    allegation = db.Column(db.String)
    # TODO: What does an allegation code look like? Should we have a mapper from
    #  int/str to user-facing language?
>>>>>>> 682aa264d7fbb0a7bdf4530e2623a07c69f3b07f
    allegation_code = db.Column(db.Integer)
    jurisdiction = db.Column(
        db.String
    )  # Should we have a jurisdiction table? Allegation Tables?
