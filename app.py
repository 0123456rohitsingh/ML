from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Success"

if __name__=="main":
    app.run(debug=True)