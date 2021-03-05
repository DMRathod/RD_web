from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '7a7d00679365b36d5e8192ecdd2b9b' 

posts = [
	{
		'author' : 'Rathod Dharmraj',
		'tittle' : 'Blog Post 1',
		'content' : 'static content1',
		'date_posted' : 'March 4th 2021'
	},
	{
		'author' : 'Meet Shekhat',
		'tittle' : 'Blog Post 2',
		'content' : 'static content2',
		'date_posted' : 'March 3th 2021'

	},
	{
		'author' : 'Hardik Vaghasiya',
		'tittle' : 'Blog Post 3',
		'content' : 'static content3',
		'date_posted' : 'March 2th 2021'

	},
	{
		'author' : 'Saurabh Balediya',
		'tittle' : 'Blog Post 4',
		'content' : 'static content4',
		'date_posted' : 'March 1th 2021'

	}
]





@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = posts)


@app.route('/about')
def about():
    return render_template('about.html',tittle='About')

@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'account created for {form.username.data}!','success')
    	return redirect(url_for('home'))
    return render_template('register.html',tittle='Register',form = form)

@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	if form.email.data == 'rd@gmail.com' and form.password.data == "root":
    		flash("You are Logged In",'success')
    		return redirect(url_for('home'))
    	else:
    	  	flash('Login Unsuccesful: please check username or password','danger')
    return render_template('login.html',tittle='Login',form = form)


if __name__ == '__main__':
	app.run(debug = True)