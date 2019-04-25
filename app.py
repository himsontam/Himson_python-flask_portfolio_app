from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os

from io import BytesIO
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import prettyplotlib as ppl
import matplotlib.pyplot as plt
from flask import flash


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)

@app.route('/reverse_sentence', methods=['GET','POST'])
def reverse_sentence_post():
    if request.method == 'GET':
	  	  return render_template('reverse_sentence.html')
    elif request.method == 'POST':
        sentence = str(request.form['text'])
        return render_template('reverse_sentence.html', result=sentence[::-1])

@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 0
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total += int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"

@app.route('/multiply_numbers', methods=['GET','POST'])
def multiply_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('multiply_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 1
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total *= int(str_num)
  	      	return render_template('multiply_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"

@app.route('/square_numbers', methods=['GET','POST'])
def square_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('square_numbers.html')
	  elif request.method == 'POST':
  	      try:
  	      	number = int(request.form['text'])
  	      	return render_template('square_numbers.html', result=number**2)
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"

@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Asia/Hong_Kong")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)


@app.route('/converter', methods=['GET','POST'])
def converter_post():
      if request.method == 'GET':
          return render_template('converter.html')
      elif request.method == 'POST':
          meters = 0.0
          try:
              value = float(request.form['text'])
              meters = (0.3048 * value * 10000.0 + 0.5) / 10000.0
              return render_template('converter.html', result=str('{:0.4f}'.format(meters)))
          except ValueError:
              return "Easy now! Let's keep it simple! 2 numbers with a space between them please"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
			if request.method == 'GET':
				return render_template('contact.html')
			elif request.method == 'POST':
				import email.utils
				from email.mime.text import MIMEText

				# Import smtplib (to allow us to email)
				import smtplib

				# set the 'from' address,
				fromaddr = str(request.form['email'])
				print(fromaddr)
				# set the 'to' addresses,
				toaddrs = ['goranmrd@gmail.com']
				tik = 'wzhvmttetwgxfngf'
				tak = tik[::-1]
				for to in toaddrs:
						msg = MIMEText('Name: '+str(request.form['name'])+'\n'+'Email: '+str(request.form['email'])+'\n'+'Phone: '+str(request.form['phone'])+'\n'+'Message: '+str(request.form['message']))
						msg.set_unixfrom('author')
						msg['To'] = email.utils.formataddr(('Recipient', to))
						msg['From'] = email.utils.formataddr(('Flask Portfolio', fromaddr))
						msg['Subject'] = 'Flask Portfolio Contact'

						# setup the email server,
						server = smtplib.SMTP('smtp.gmail.com', 587)
						server.starttls()
						server.login("lokhimtamhimson@gmail.com", tak)

						# Print the email's contents
						print('From: ' + fromaddr)
						print('To: ' + str(to))
						print('Message: ' + msg.as_string())

						# send the email
						server.sendmail(fromaddr, to, msg.as_string())
						# disconnect from the server
						server.quit()
				try:
					flash('Message sent!')
					return render_template('contact.html')
				except Exception as e:
					flash(e)
					return render_template('contact.html')
         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)
