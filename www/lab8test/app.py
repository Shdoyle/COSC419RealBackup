import random
import functools

from flask import Flask, render_template, Markup, request, session, url_for, flash, g, redirect, abort, redirect

MyApp = Flask(__name__)

MyApp.secret_key = "blkdlweew42l23"

#Templates
@MyApp.route("/template")
def template():
  return render_template('template.html')

#extends template
@MyApp.route('/')
def default():
  return render_template('home.html')

@MyApp.route('/home')
def home():
  return redirect('/')

@MyApp.route("/login")
def login():
  return render_template('login.html')

@MyApp.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']    
  else:
    username = "No POST"
  if username == "admin":
    if password == "admin":
      session['username'] = username
      usernamepassed = session['username'] 
  else :
    flash('Error : Login Failed. Please try again.')
    return redirect('/')
  return render_template('profilepage.html')

 
@MyApp.route('/profile')
def profile():
  if session['username']:
    return render_template('profilepage.html')  
  else : 
    flash('Error : No Access')
    return redirect('/')

@MyApp.route('/logout')
def logout():
  session.clear()
  return render_template('logout.html')
  
@MyApp.route('/editprofile')
def editprofile():
  flash('Error : Edit Profile is not enabled yet.')
  return redirect('/')
  
@MyApp.route("/signup")
def signup():
  return render_template('signup.html')

@MyApp.route("/page1")
def page1():
  return render_template('page1.html')

@MyApp.route("/page2")
def page2():
  return render_template('page2.html')
  
@MyApp.route("/contact")
def contact():
  return render_template('contact.html')

@MyApp.route("/about")
def about():
  return render_template('about.html')
  
@MyApp.errorhandler(403)
def forbiddenerror():
  return render_template('403_page.html'), 403
  
@MyApp.errorhandler(404)
def forbiddenerror():
  return render_template('403_page.html'), 404
   
if __name__=="__main__":
	MyApp.run()