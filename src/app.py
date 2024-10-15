from http.client import responses
from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '9dc412785a84fdf9b80ac3e02bb3f75c'


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'green-500')
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful.Please check username and password','red-500')
    return render_template("login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'green-500')
        return redirect(url_for('login'))

    return render_template("register.html", form=form)


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/properties')
def properties():
    return render_template("properties.html")


@app.route('/tenants')
def tenants():
    return render_template("tenants.html")

if __name__ == '__main__':
    app.run(debug=True)
