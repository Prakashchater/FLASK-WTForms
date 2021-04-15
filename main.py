from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    # email = StringField('email', [
    #     validators.Length(min=6, message=(u'Little short for an email address?')),
    #     validators.Email(message=('Invalid Email address.'))
    # ])
    email = StringField(label='email', validators=[DataRequired(), Email()])

    # password = PasswordField('password', [
    #     validators.Length(min=8, message=('Field must be at least 8 character long.'))
    #
    # ])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=6)])

    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "qwertyuiop"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = MyForm()       #calling the class
    if login_form.validate_on_submit():
        if login_form.email.data == "chater@gmail.com" and login_form.password.data == "123456789":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)