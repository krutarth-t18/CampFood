from CampFood import db
from flask_login import UserMixin


class Registration(db.Model,UserMixin):
    Sno = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    ph_no = db.Column(db.BIGINT, nullable=False)


class Items(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    item_img = db.Column(db.String(200), nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    cat_id = db.Column(db.String(50), db.ForeignKey('category.foreign_id'), nullable=False)


