from flask import Flask,request,jsonify

#app name define

pracApp = Flask(__name__)

@pracApp.route("/")
def homepage():
    return "welcome practice"

@pracApp.route("/operation",methods=['POST']) 
def add():
    if request.method=="POST":
        result=int(request.json['num1'])+int(request.json['num2'])
        return jsonify("the sum is {}".format(result))




if __name__=="__main__":
    pracApp.run(host="0.0.0.0",port=5000)
