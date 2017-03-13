from app import app, table_manager, price_tracker
from flask import render_template, flash, redirect, session, request
from .forms import LoginForm, ProductDetailForm
import hashlib


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if 'username' in session:
        username = session['username']
        form = ProductDetailForm()
        if form.validate_on_submit():
            print "Entered into prod form validation"
            prod_link = request.form['product'].strip()
            prod_details = price_tracker.getProductDetails(prod_link)
            if prod_details == -1:
                flash("Invalid link")
            elif prod_details[0] != "Amazon.com":
                flash("Not an Amazon product")
            elif prod_details[2] == None:
                flash("Sorry! Couldn't find the price of your product, We're already looking into it. You'll receive an email soon")
            else:
                flash("Your product " + prod_details[1] + " has a current price of " + prod_details[2] + ". We'll track the price and will notify you if it goes up or down. Thanks for using Amazon Price Tracker!")

        return render_template('index.html', username=username, form=form)

    if form.validate_on_submit():
        print "Entered here"
        uname = request.form['username']
        pword = request.form['password']
        hashed_pword = hashlib.sha512(pword).hexdigest()
        check_user_result = table_manager.check_user(uname, hashed_pword)
        if check_user_result == 10 or check_user_result == 12:
            session['username'] = uname
            return redirect('/')
        elif check_user_result == 11:
            form.password.errors.append("Invalid password. Please try again")
        else:
            print check_user_result
            form.password.errors.append(
                "Unexpected issue. Please try again later")

    return render_template("initialindex.html", form=form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
