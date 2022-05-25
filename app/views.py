from flask import render_template, request
from app import app
import datetime

@app.route('/template')
def template():
    return render_template('home.html')


@app.route('/')
def home():
   return "hello world!"


@app.route('/hora')
def horas():
    return str(datetime.datetime.now())

@app.route('/soma')
def template():
    return render_template('soma.html')

@app.route('/soma', methods=['POST'])
def my_form_post():
    n1 = request.form['numero1']
    n2 = request.form['numero2']

    return f"a soma dos dois numero deu {float(n1) + float(n2)}"
