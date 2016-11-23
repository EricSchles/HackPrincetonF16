import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
#from imageverify import main

from flask.ext.sqlalchemy import SQLAlchemy
import os
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    success = db.Column(db.String(400))

    def __init__(self,success):
        self.success = success

    def __repr__(self):
        return "<success reached {}>".format(self.success)
        

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello():
    user = request.args.get('content')
    import code
    code.interact(local=locals())
    status = main(user)
    return status

@app.route("/get_data",methods=["GET","POST"])
@cross_origin()
def get_data():
    if request.method=="POST":
        test = Test("got here")
        db.session.add(test)
        db.session.commit()
        #json_data = request.json
        #data = request.data
    return "done"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
