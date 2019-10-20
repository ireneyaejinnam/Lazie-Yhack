from flask import Flask, render_template, url_for, redirect, session
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine 
from mongoengine import StringField, EmailField

#from form import LoginForm
from form import LoginForm
#from form import EntryForm

app = Flask(__name__)
app.config['DEBUG'] = True #every time you run an error, it will show an error message; without this line, the server will crash and you won't know why
app.config['SECRET_KEY'] = 'SOME_STRING_THATS_SECRET'

bootstrap = Bootstrap()
bootstrap.init_app(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'yhack-db',
    'host': 'ds125906.mlab.com',
    'port': 25906,
    'username': 'admin',
    'password': 'gocolumbia2021'
}

db = MongoEngine()
db.init_app(app)

"""
login_manager = LoginManager()
login_manager.init_app(app)
"""

"""
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
#should return None (not raise an exception) if the ID is not valid
"""

class User(db.Document):
	name = StringField(required=True)
	uni = StringField(required=True)
	password = StringField(required=True)
	email = EmailField(required=True)
	phone = StringField(required=True)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User(name=form.name.data, uni=form.uni.data, password=form.password.data, email=form.email.data, phone=form.phone.data)
		user.save()

		redirect(url_for('login')) 
	return render_template('login.html', form=form)

"""
@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():

		login_user(user)

		flask.flash('')

		session['uni'] = form.uni.data
		session['password'] = form.password.data

		if db.getCollectionInfos( { uni: session['UNI'] } ):
			if db.getCollectionInfos( { password: session[''] })
"""

"""
class Entry(db.Document):
	author = StringField(required=True) #new Entry has to have author defined
	content = StringField()

@app.route('/')
def home():
	return render_template('home.html', name='Alice', my_friends={'jonathan': 68, 'cesar': 62, 'nick': 100})

@app.route('/diary', methods=['GET','POST'])
def diary():
	form = EntryForm() #create new instance
	if form.validate_on_submit():
		entry = Entry(author=form.author.data, concent=form.content.data)
		entry.save()

		redirect(url_for('diary'))
	return render_template('diary.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login(): #create decorator
	username = None
	form = LoginForm()
	if form.validate_on_submit():
		session['uni'] = form.uni.data
		session['password'] = form.password.data
		print session.get('uni')
		return redirect(url_for('login'))
	return render_template('login.html', form=form, uni=session.get('uni'), name=session.get('password'))
"""

if __name__ == "__main__": #main is magic variable
	app.run() 
