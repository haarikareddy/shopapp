from flask import Flask, render_template, request
import csv

data = open("dress.csv")
data = csv.reader(data)
data1 = []
for row in data:
    data1.append([row[1],row[3]]) 
for item in data1:
    print(item)  

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    catego= request.form['cat']
    for i in range(len(data1)):
        if catego == data1[i][0]:
            ucat = data1[i][1]
            print(ucat)
    print(catego)
    return render_template('pass.html',c=catego,u=ucat)

if __name__=='__main__':
    app.run(debug=True,port=5000)