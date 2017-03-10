from app import app
from flask import render_template, flash, redirect, session, request
from .forms import LoginForm


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    print "Entered"
    form = LoginForm()

    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)

    if form.validate_on_submit():
        print "Entered22"
        uname = request.form['username']
        pword = request.form['password']
        # Add database checks and update correspondingly
        session['username'] = uname
        return redirect('/')
    return render_template("initialindex.html", form=form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
