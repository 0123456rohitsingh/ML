from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Successfull Development of CI/CD Pipeline"

if __name__=="main":
    app.run(debug=True)