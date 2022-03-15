from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from CampFood.main import Micro

app = Flask(__name__)
app.config['SECRET_KEY'] = 'show'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/campfood_webapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def main():
    show_data = Micro.query.all()
    return render_template('show.html', show_data=show_data)


if __name__ == '__main__':
    app.run(debug=True, port=6500)
