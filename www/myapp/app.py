import random

from flask import Flask, render_template, Markup, request
MyApp = Flask(__name__)

#Lab6
@MyApp.route("/")
def helloworld():
	return "<h1>Hello World!</h1>"

#Lab6
@MyApp.route("/lottery")
def lottery():
	winner = 777
	yourNumber = random.randint(0,999)
	if yourNumber == winner:
		outputString = "<h1>Ladies and Gentlemen... We have a WINNER!!!</h1><br><p>Your Number is %d .</p>" % (yourNumber)
	else:
		outputString = "<h1>Sorry</h1><br><p>Your Number was %d . Try again!</p>" % (yourNumber)
	return outputString

#Lab6
@MyApp.route("/lotto")
def lotto():
	winner = 777
	yourNumber = random.randint(0,999)
	if yourNumber == winner:
		outputString = "Ladies and Gentlemen... We have a WINNER!!!"
	else:
		outputString = "Sorry"
	return render_template('lotto.html', outMessage=outputString, randomNumber=yourNumber, winningNumber=winner) 

#Lab7
@MyApp.route("/random")
def myrandom():
  myWin = 7
  myRan = random.randint(0,9)
  BGC="blue"
  if myRan == myWin:
    myOut = "You Are A Winner!"
    BGC="red"
  else:
    myOut = "Sorry"
  data = "<p>It was the <strong>best</strong> of times, it was the <strong>worst</strong> of times.</p>" 
  markedData = Markup(data)   
  return render_template('random.html', myMsg=myOut, myRandom=myRan, myWinning=myWin, myData=markedData, myBGC=BGC)

#Lab7
@MyApp.route('/routes/<var>')
def routesFunc(var=None):
  upperVar = var.upper()
  return render_template('displaydata.html', head1="/routes/<var>", msg=upperVar)
  
#Lab7
@MyApp.route('/routes/<var>/<var2>')
def routesFunc2(var=None, var2=None):
  upperVar = var.upper()
  return render_template('displaydata.html', head1="/routes/<var>/<var2>", msg=upperVar + var2)

#Lab7
@MyApp.route('/reqType', methods=['GET', 'POST'])
def reqType():
  if request.method == 'POST':
    outString = "This is a POST request!"
  else: 
    outString = "This is a GET request!"
  return outString
    
#Lab7
@MyApp.route('/form')
def form():
  return render_template('input.html')

#Lab7
@MyApp.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    inputString = request.form['input']
    length = len(inputString)
    outString = str(length)
    return outString
  
#Lab7
@MyApp.route('/getTest', methods=['GET'])
def getTest():
  if request.method == 'GET':
    tString = request.args.get('key')
    return tString
  
#Templates
@MyApp.route("/template")
def template():
  return render_template('template.html')

#extends template
@MyApp.route("/displaydata")
def displaydata():
  return render_template('displaydata.html', head1="The Return Value is", msg="The Data")

#test.html has copied code from W3, I used it as a template when making my page. This was not my writing.
@MyApp.route("/test")
def test():
	name="Shane"
	return render_template('test.html', name=name)
 
#I'm just hosting a couple pictures here
@MyApp.route("/pizza1")
def pizza1():
   return render_template('pizza1.html')
  
if __name__=="__main__":
	MyApp.run()
