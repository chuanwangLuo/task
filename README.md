#Flask
Data from database: World Development Indicators

## Design
This application is designed to provide a user-friendly interface through which users can view and 
analyze statistics for different countries in different years. Based on Flask framework, 
the system uses flask-SQLalchemy for database operation and flask-migrate for database migration. 
Data is stored and manipulated by defining two main models: Country and Series.

- ** Back-end ** : Flask
- ** Database ** : SQLite, managed by SQLAlchemy
- ** Front end ** : Jinja2 template, Bootstrap for styling

### Database design
Database migration
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

The system designs two main database models:

- 'Country' : Stores country information, such as the country name and country code.
- 'Series' : Stores statistical sequence information, such as series name and series code.
- 'Record' : Stores specific statistical data records, including years and values, associated with 'Country' and 'Series'.

These models realize the relationship between data through foreign key association, and facilitate query and analysis.

##
pip install Flask-SQLAlchemy
pip install Flask-Migrate

###Example Initialize the migration directory
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

##base template: base.html
base.html usually contains the common structure of the website, such as the header, navigation bar, and foot, as well as the introduced CSS and JavaScript files. 
Other templates can inherit base.html to avoid repeating this generic code.

##Use Git for source control
git init
git add .
git commit -m 

#Check the branch you are currently in
git branch
git checkout master


### Deploy to Render

This application has been successfully deployed to Render, where 'Procfile' is used to specify the startup command as' gunicorn app:app '. 
In the setup of Render, the necessary environment variables such as the database path are also configured.

Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

Installation dependency
pip install -r requirements.txt
But in the requirement. txt need to dataclasses==0.6, because the current python version is 3.6, the generated requirement is 0.8, the deployment error.
pkg_resources==0.0.0 also need to delete

##Push to remote repository
git remote add origin <https://github.com/chuanwangLuo/task.git>
git push -u origin master







