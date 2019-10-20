from flask import Flask, render_template, url_for, redirect, session
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine 
from mongoengine import StringField, EmailField, BooleanField

from form import LoginForm
from form import AskForm

app = Flask(__name__)
app.config['DEBUG'] = True #every time you run an error, it will show an error message; without this line, the server will crash and you won't know why
app.config['SECRET_KEY'] = 'SOME_STRING_THATS_SECRET' #???

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

class User(db.Document):
	name = StringField(required=True)
	uni = StringField(required=True)
	password = StringField(required=True)
	email = EmailField(required=True)
	phone = StringField(required=True)

class Ask(db.Document):
	task = StringField(required=True)
	descr = StringField(required=True)
	reward = StringField(required=True)
	askerid = StringField() #why can't required be true??
	doerid = StringField()
	isTaken = BooleanField()
	isCompleted = BooleanField()

@app.route('/login', methods=['GET','POST']) #delete 'GET'
def login():
	form = LoginForm()
	if form.validate_on_submit():
		name=None
		uni=None
		password=None
		email=None
		phone=None

		user = User(name=form.name.data, uni=form.uni.data, password=form.password.data, email=form.email.data, phone=form.phone.data)
		user.save()

		#session['name'] = user.name
		#session['uni'] = user.uni
		#session['password'] = user.password
		#session['email'] = user.email
		#session['phone'] = user.phone

		session['userid'] = str(user['id']) #.str??

		redirect(url_for('home')) #???
	return render_template('login.html', form=form, userid=session.get('userid'))

@app.route('/')
def home():
	#if they click on one button it redirects to __, otherwise redirects to __
	return render_template('home.html')

@app.route('/ask', methods=['GET','POST'])
def ask():
	task=None
	descr=None
	reward=None
	askerid=None
	doerid=None
	isTaken=False
	isCompleted=False

	form = AskForm()
	if form.validate_on_submit():
		ask = Ask(task=form.task.data, descr=form.descr.data, reward=form.reward.data, askerid=session.get('userid'), doerid=None, isTaken=False, isCompleted=False)
		ask.save()

		redirect(url_for('me'))
	return render_template('ask.html', form=form)

@app.route('/do', methods=['GET','POST'])
def do():
	available_asks = Ask.objects(isTaken =False, isCompleted= False);
	#all_asks_list = available_asks.toArray()
	#session['all_asks_list'] = all_asks_list
	#redirect(url_for('do'))
	return render_template('do.html', all_asks_list=available_asks)

@app.route('/me', methods=['GET','POST'])
def me():
	my_asks = Ask.objects(askerid=session.get('userid') )
	#my_asks_list = my_asks.toArray()
	#session['my_asks_list'] = my_asks_list
	
	my_dos = Ask.objects(doerid=session.get('userid') )
	#my_dos_list = my_dos.toArray()
	#session['my_dos_list'] = my_dos_list
	
	return render_template('me.html', my_asks_list=my_asks, my_dos_list=my_dos)

if __name__ == "__main__": #main is magic variable
	app.run() 
