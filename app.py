from flask import Flask,request


#name define
app =Flask(__name__)

#handle request by route
@app.route("/")#route / means home page

# handle route define function
def Hello_Word():
    return "Hello World"

@app.route('/aboutUs')
def aboutUs():
    return "this is Kiran"

#second peramiter get post
#@app.route('/contactUs',methods=['GET','POST'])
@app.route('/demo',methods=['POST'])
def demo():
    if request.method=='POST':
        operation=request.json["operation"]
        num1=request.json["num1"]
        num2=request.json["num2"]
        result=0
        '''result=num1 + num2

        return "the operation is {} and the result is {}".format(operation,result)
        

@app.route('/multiply',methods=['POST'])
def multi():
    if request.method=='POST':
        operation=request.json["operation"]
        num1=request.json["num1"]
        num2=request.json["num2"]
        result=num1 * num2

        return "the operation is {} and the result is {}".format(operation,result)
     
''' 
    if operation=="add":
        result=num1+num2
    elif operation=="muliply" :
        result=num1*num2
    elif operation=="divide"  :
        result=num1/num2

    else :
        result=num1-num2     

    return "the operation is {} and the result is {} ".format(operation,result)      


#private variable entry point
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
