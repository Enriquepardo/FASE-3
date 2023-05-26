from utils.db import db
from sqlalchemy.schema import CheckConstraint

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone

__table_args__ = (
    CheckConstraint('char_length(email) >= 5', name='email_len_check'),
    CheckConstraint('char_length(phone) >= 10', name='phone_len_check'),
)
