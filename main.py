from flask import Flask,render_template, redirect ,request
import csv
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data = []
        file = request.files['file'] 
        if file:
            for line in file:
                row = line.decode('utf-8').strip().split(',') 
                data.append(row)
            return render_template('table.html',L=data)
        else:
            return render_template('index.html')
app.run(debug=True)