from requests import get
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

#Initialize Flask Application
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
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

#Access Github api and retrieve repository information
def build_db():
	db.create_all()
	req = get('https://api.github.com/search/repositories?q=topic:python&sort:stars&page=3&per_page=100')
	count = req.json()['total_count']
	page = 1
	while count > 0:
		req = get('https://api.github.com/search/repositories?q=topic:python&sort:stars&page={page}&per_page=100'.format(page=page))
		jsonReq = req.json()['items']
		count -= 100
		page += 1
		for project in jsonReq:
#			exists = db.session.query(Repository.id).filter_by(id=project['id']).scalar() is not None
			temp = Repository(project['id'],project['name'],project['url'],project['created_at'],project['pushed_at'],project['description'],project['stargazers_count'])
			db.session.add(temp)
			db.session.commit()

#Create route for homepage
@app.route("/")
def home_page():
	repo = Repository.query.order_by(Repository.stars.desc())
	return render_template('RepoTable.html', repo = repo)

if __name__ == "__main__":
	app.run()
	
