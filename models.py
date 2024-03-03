from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):#User class represents a user. It inherits from db.Model, meaning it is a database model.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):#Task class represents a task. It also inherits from db.Model.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user_id is a foreign key that points to the id field of the User table and establishes the relationship between Task and User.
    def __repr__(self):
        return f'Task(id={self.id}, title={self.title})'
#The __repr__ method defines the string representation of this class

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(3), unique=True, nullable=False)
    records = db.relationship('Record', backref='country', lazy=True)

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    records = db.relationship('Record', backref='series', lazy=True)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    year2021 = db.Column(db.Float, nullable=True)
    year2022 = db.Column(db.Float, nullable=True)
