from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/campfood_webapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Items(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    item_img = db.Column(db.String(200), nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    cat_id = db.Column(db.String(45), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        item_id = request.form['item_id']
        cat_id = request.form['cat_id']
        data = Items.query.filter_by(item_id=cat_id).first()
        if data.item_id == item_id:
            data.cat_id = cat_id
        db.session.add(data)
        db.session.commit()
    show_data = Items.query.all()
    return render_template('index.html', show_data=show_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
