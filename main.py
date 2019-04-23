from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, AddActivityForm, EditActivityForm, CreateTemplateForm

#This is for flask to know where to look for, ___ is used in python
app = Flask(__name__)
#secretkey to validate input of users
app.config['SECRET_KEY'] = '900eb407f68967dfa80ad5f0ff13a46d'

#decorator that allows us to write the function to return the website
@app.route("/") 
def post():
    return render_template('post.html')

@app.route("/home")
def home():
    return render_template('home.html')
    
@app.route("/about") 
def about(): 
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST']) 
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}! \r\n You can add your activities now!', 'success')
    	# returns user to the page you say after it was successful
    	return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	#dummy data to verify is working
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/addActivity", methods=['GET', 'POST']) 
def addActivity(): 
    form = AddActivityForm()
    if form.validate_on_submit():
    	flash(f'Activity created', 'success')
    	# returns user to the page you say after it was successful
    	return redirect(url_for('home'))
    return render_template('addActivity.html', title='Add Activity', form=form)

@app.route("/editActivity", methods=['GET', 'POST']) 
def editActivity(): 
    form = EditActivityForm()
    if form.validate_on_submit():
    	flash(f'Activity edited', 'success')
    	# returns user to the page you say after it was successful
    	return redirect(url_for('home'))
    return render_template('editActivity.html', title='Edit Activity', form=form)

@app.route("/createTemplate", methods=['GET', 'POST']) 
def createTemplate(): 
    form = CreateTemplateForm()
    if form.validate_on_submit():
    	flash(f'Activity Created with New Template', 'success')
    	# returns user to the page you say after it was successful
    	return redirect(url_for('home'))
    return render_template('createTemplate.html', title='Create New Template', form=form)
    
#This conditional is true if we run the script directly
if __name__ == "__main__":
    app.run(debug=True)
