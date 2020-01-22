import os
from flask import Flask, request, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *
from flask_migrate import Migrate
from weather import *

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = f"sqlite:///{os.path.join(project_dir, 'weather.db')}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Forecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    coord_lon = db.Column(db.Float)
    coord_lat = db.Column(db.Float)

    positive = db.Column(db.Boolean)

    weather_id = db.Column(db.Integer)
    weather_main = db.Column(db.String(200))
    weather_description = db.Column(db.String(200))
    weather_icon = db.Column(db.String(200))
    base = db.Column(db.String(200))
    main_temp = db.Column(db.Float)
    main_feels_like = db.Column(db.Float)
    main_temp_min = db.Column(db.Float)
    main_temp_max = db.Column(db.Float)
    main_pressure = db.Column(db.Integer)
    main_humidity = db.Column(db.Integer)
    main_sea_level = db.Column(db.Integer)
    main_grnd_level = db.Column(db.Integer)
    visibility = db.Column(db.Integer)
    wind_speed = db.Column(db.Float)
    wind_deg = db.Column(db.Integer)
    clouds_all = db.Column(db.Integer)
    rain_1h = db.Column(db.Float)
    rain_3h = db.Column(db.Float)
    snow_1h = db.Column(db.Float)
    snow_3h = db.Column(db.Float)
    dt = db.Column(db.Integer)
    sys_type = db.Column(db.Integer)
    sys_id = db.Column(db.Integer)
    sys_message = db.Column(db.String(200))
    sys_country = db.Column(db.String(200))
    sys_sunrise = db.Column(db.Integer)
    sys_sunset = db.Column(db.Integer)
    timezone = db.Column(db.Integer)
    name = db.Column(db.String(200))
    cod = db.Column(db.Integer)
    
    def __rep__(self):
        return f"<ID:{self.id}\tPositive:{self.positive}>"

@app.route("/", methods=["GET","POST"])
def home():
    if request.form:
        #forecast = Forecast(coord_lon=request.form.get("lon"), coord_lat=request.form.get("lat"), positive=bool(request.form.get("positive")))
        lat = request.form.get("lat")
        lon = request.form.get("lon")
        
        w_data = flatten_dictionary(get_current_weather(lat, lon))
        del w_data['id'] # remove the id gathered from the weather api
        forecast = Forecast(**w_data)
        forecast.positive = bool(request.form.get('positive'))
        print(forecast.id)
        db.session.add(forecast)
        db.session.commit()
    forecasts = Forecast.query.all()
    return render_template("home.html", forecasts=forecasts, f=Forecast)

@app.route("/update", methods=["POST"])
def update():
    forecast_id = request.form.get("id")
    newpositive = bool(request.form.get("newdisposition"))
    forecast = Forecast.query.get(forecast_id)
    forecast.positive = newpositive
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    forecast_id = request.form.get("id")
    forecast = Forecast.query.get(forecast_id)
    db.session.delete(forecast)
    db.session.commit()
    return redirect("/")

@app.route('/results/')
def results():
    data = Forecast.query.all()
    result = [d.__dict__ for d in data]
    return jsonify({'test':20})

if __name__ == "__main__":
    app.run() 