from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

#trdf@app.route('/<username>')
#def user(username=None):
#    return render_template('indexuser.html', name=username)

#app.route('/<username>/<post_id>')
#def posts(username=None, post_id=None):
#    return render_template('index.html', post_num=post_id)

@app.route('/<string:pagename>')
def home(pagename):
    return render_template(pagename)
'''
@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/about.html')
def about():
    return render_template('about.html')
'''
def write_to_file(data):
	with open('database.txt' , mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'email: {email}\nsubject: {subject}\nmessage: {message}\n')

def write_to_csv(data):
	with open('database.csv' , mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong somewhere. Try again!'


