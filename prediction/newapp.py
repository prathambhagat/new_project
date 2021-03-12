from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import json

app = Flask(__name__)

with open('mylogreg.json') as f:
	data = json.load(f)
accuracy=data['acc_out']
summ=data['summ']

@app.route('/')
def hello_world():
    return render_template("sample.html",accuracy=accuracy,summ=summ)


if __name__ == '__main__':
    app.run(debug=True)

