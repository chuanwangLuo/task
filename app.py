from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Task, Country, Series, Record
from flask import render_template, request, redirect, url_for
#Import the Flask class as well as other Flask extensions such as SQLAlchemy and Migrate for database manipulation and migration
# Import the model defined from the models file
#Import Flask's auxiliary tools such as render_template, request, redirect, and url_for for handling HTTP requests and responses

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
##Example Create a Flask application instance.
##Configure the SQLite database URI used by SQLAlchemy.
##Turn off SQLAlchemy's change tracking to improve performance.
db.init_app(app)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Hello, World!"
#defines the root route of the application, which returns a simple welcome message.

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)
#displays a list of all users.

@app.route('/user/new')
def new_user():
    return render_template('new_user.html')
#displays the form for creating a new user.

@app.route('/user/add', methods=['POST'])
def add_user():
    name = request.form['name']
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('list_users'))
#handles form submissions to add a new user.

@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        db.session.commit()
        return redirect(url_for('list_users'))
    return render_template('edit_user.html', user=user)
#Displays and processes forms for editing user information.

@app.route('/user/delete/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('list_users'))
#andles the request to delete the user.

@app.route('/task/<int:id>')
def task_detail(id):
    task = Task.query.get_or_404(id)
    return render_template('task_detail.html', task=task)
#displays detailed information about a specific task.

@app.route('/task/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.content = request.form['content']
        db.session.commit()
        return redirect(url_for('task_detail', id=task.id))
    return render_template('edit_task.html', task=task)
#displaying and processing edit task information.

@app.route('/task/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
#handles requests to delete tasks.

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
#@app.errorhandler(404) defines an errorhandler for handling 404 (page not found) errors, displaying a custom 404 error page.
#@app.errorhandler(500) defines an errorhandler for handling 500 (internal server error) errors, displaying a custom 500 error page
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('errorlog.txt', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
# If the application is not in debug mode, set up a log handler to record error messages to a file

if __name__ == '__main__':
    app.run(debug=True)
# The code checks to see if the script runs directly, and if so, launches the Flask application
