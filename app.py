from distutils.log import debug
from urllib import response
from flask import Flask, jsonify, render_template, request
from program import WaterJugProblem

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html',per=20)

@app.route("/play",methods=['GET','POST'])
def play():
    data = [int(x) for x in request.get_json()] 
    print(request.get_json())
    obj = WaterJugProblem(data[0],data[1],data[2],data[3],data[4],data[5])
    s = obj.run_program()
    print(s)
    if s!='NOT POSSIBLE':
        s = [list(x) for x in s]
        return jsonify(s)
    else:
        return jsonify(s)


app.run(debug = True)