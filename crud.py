from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql import func, select
import os
import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/datacatcher_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now()) 
    tmp = db.Column(db.String(80))
    hum = db.Column(db.String(120))
    lux = db.Column(db.String(120))
    prs = db.Column(db.String(120))

    def __init__(self, tmp, hum, lux, prs):
        self.tmp = tmp 
        self.hum = hum 
        self.lux = lux 
        self.prs = prs 


class RecordSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('date','tmp', 'hum', 'lux', 'prs')


record_schema = RecordSchema()
record_schema = RecordSchema(many=True)


# endpoint to create new user
@app.route("/record", methods=["POST"])
def add_record():
    print(request.json)
    tmp = request.json['tmp']
    hum = request.json['hum']
    lux = request.json['lux']
    prs = request.json['prs']
    new_record = Record(tmp, hum, lux, prs)

    db.session.add(new_record)
    db.session.commit()
    return jsonify(str(new_record))


# endpoint to show all users
@app.route("/record", methods=["GET"])
def get_record():
    #last_record = Record.query.all()
    last_record = Record.query.order_by('date desc').limit(1)
    result = record_schema.dump(last_record)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/record/<id>", methods=["GET"])
def record_detail(id):
    record = Record.query.get(id)
    return record_schema.jsonify(record)


# endpoint to delete user
@app.route("/record/<id>", methods=["DELETE"])
def record_delete(id):
    record = Record.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return record_schema.jsonify(record)


if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0')
