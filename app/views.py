from flask import render_template, flash, redirect
from flask_login import (LoginManager, login_required, login_user, 
                         current_user, logout_user, UserMixin)
from app import app
from app import lm
from .forms import *
import flask_login
from models import *
from flask import request



@lm.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id).first()

@lm.unauthorized_handler
def unauthorized():
    # do stuff
    return 'unauthorized palceholder'


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'username': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'username': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/about')
@login_required
def about():
	return render_template('about.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() 
    if request.method == 'POST' and form.validate():
    	user = User.query.filter_by(username=form.username.data).first() 
    	if user and user.validate_password(form.password.data):
    		login_user(user)
        	return redirect('/index')

    if current_user.is_authenticated:
    	return redirect('/index')

    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/register', methods=['GET','POST'])
def register():
	form = SignupForm()
	if request.method == 'POST' and form.validate():
		user = User.query.filter_by(username=form.username.data).first()
		em_user = User.query.filter_by(email=form.email.data).first()
		if not user and not em_user:
			new_user = User(username=form.username.data,password=form.password.data,email=form.email.data)
			db.session.add(new_user)
			db.session.commit()
			return redirect('/login')
	return render_template('register.html',
								title='Register',
								form=form)


