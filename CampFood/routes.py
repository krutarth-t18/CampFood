from flask import render_template, url_for, redirect, flash, session, request
from flask_login import login_required, LoginManager, login_manager
from CampFood.models import Registration, Items
from CampFood.forms import RegisterForm, LoginForm, UpdateForm
from CampFood import db
from CampFood import app


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    show_data = Items.query.all()
    #
    # if form.validate_on_submit():
    #     register = Registration(fullname=form.fullname.data, username=form.username.data,
    #                             password=form.confirm_password.data, ph_no=form.ph_no.data)
    #     db.session.add(register)
    #     db.session.commit()
    #     return redirect('/signin2')

    return render_template('index.html', form=form, show_data=show_data)


@app.route('/signup2', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        register = Registration(fullname=form.fullname.data, username=form.username.data,
                                password=form.confirm_password.data, ph_no=form.ph_no.data)
        db.session.add(register)
        db.session.commit()
        return redirect('/home')
    return render_template('signup2.html', form=form)


@app.route('/signin2', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        record = Registration.query.filter_by(username=form.username.data).first()
        if record and record.password == form.password.data:
            return redirect(url_for('home', Sno=record.Sno))
        else:
            flash("Incorrect username/password!")
    return render_template('signin2.html', form=form)


@app.route('/home/<int:Sno>', methods=['GET', 'POST'])
# @login_required
def home(Sno):
    show_data = Items.query.all()
    record = Registration.query.filter_by(Sno=Sno).first()
    return render_template('home.html', record=record, show_data=show_data)


@app.route('/signout')
def signout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect('/signin2')


@app.route('/update/<int:Sno>', methods=['GET', 'POST'])
def update(Sno):
    form = UpdateForm()
    record = Registration.query.filter_by(Sno=Sno).first()
    Pass = record.password
    if form.validate_on_submit():
        record.username = form.username.data
        if form.confirm_password.data != "":
            if form.current_password.data == "":
                flash("Enter your current password first!")
            if record.password != form.current_password.data:
                flash("Incorrect current password.")
        else:
            if form.confirm_password.data == "":
                record.password = Pass
            else:
                record.password = form.confirm_password.data
            db.session.add(record)
            db.session.commit()
            return redirect('/signin2')
    return render_template('update.html', form=form, record=record)


@app.route('/delete/<int:Sno>')
def delete(Sno):
    record = Registration.query.filter_by(Sno=Sno).first()
    db.session.delete(record)
    db.session.commit()
    return redirect('/')


@app.route('/cart/<int:Sno>')
def cart(Sno):
    # cart_data = Items.query.all()
    # record = Registration.query.filter_by(Sno=Sno).first()
    return render_template('cart.html', Sno=Sno)
