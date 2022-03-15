from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'items'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/campfood_webapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Micro(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ph_no = db.Column(db.String(15), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        name = request.form.get('name')
        ph_no = request.form.get('ph_no')
        data = Micro(name=name, ph_no=ph_no)
        db.session.add(data)
        db.session.commit()
        return redirect('/')
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, port=5500)
