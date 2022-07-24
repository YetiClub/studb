import os
from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PhoneNumber
import json
from flask_marshmallow import Marshmallow
# from flask_migrate import Migrate


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "studentdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
ma = Marshmallow(app)
# migrate = Migrate(app, db)


class Staff(db.Model):
    user_name = db.Column(db.String(80), unique=False,
                           nullable=False, primary_key=False)
    password = db.Column(db.String(80), unique=False,
                          nullable=False, primary_key=False)
    role = db.Column(db.Integer, unique=True,
                        nullable=False, primary_key=True)
    userId = db.Column(db.String, unique=True,
                      nullable=False, primary_key=False)
    referral_code_id = db.Column(db.Unicode(
        255), unique=True, nullable=False, primary_key=False)

    def __repr__(self):
        return "<User Name: {}, Role {}, UserId: {}, Password: {}, Referral Code Id: {} >".format(self.user_name, self.user_id, self.role, self.referral_code_id, self.phone_number, self.password)


class StaffSchema(ma.Schema):
    class Meta:
        fields = ('user_name', 'user_id',
                  'role', 'referral_code_id', 'password')


staff_schema = StaffSchema(many=True)


@app.route('/')
def start():
    return jsonify('Pong!')


@app.route('/getstaff', methods=["GET", "POST"])
def home():
    staff = Staff.query.all()
    result = staff_schema.dump(staff)
    print(result[0]['role'])
    return jsonify(result)


@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers",
                         "Content-Type,Authorization")
    return response


if __name__ == "__main__":
    app.run(debug=False)
