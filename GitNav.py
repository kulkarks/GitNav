from requests import get
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

#Initialize Flask Application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC12345ksk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Repositories.db'
app._static_folder = '//static/'

db = SQLAlchemy(app)

#Define repository class
class Repository(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	url = db.Column(db.String)
	created_date = db.Column(db.String)
	last_push = db.Column(db.String)
	description = db.Column(db.String)
	stars = db.Column(db.Integer)


	def __init__(self, id, name, url, created_date, last_push, description, stars):
		self.id = id
		self.name = name
		self.url = url
		self.created_date = created_date
		self.last_push = last_push
		self.description = description
		self.stars = stars

#Create route for homepage
@app.route("/")
def home():
	repo = Repository.query.order_by(Repository.stars.desc())
	return render_template('RepoTable.html', repo = repo)

if __name__ == "__main__":
	app.run()
	
