
from flask import Flask
from flask_migrate import Migrate, Manager, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from db_credentials import SQL_USER, SQL_HOST,SQL_PASS, SQL_DB

app = Flask(__name__)
app.secret_key = "login key"

# database
db_url = 'mysql+pymysql://' + SQL_USER + ':' + SQL_PASS + '@' + SQL_HOST + '/' + SQL_DB
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize db
db = SQLAlchemy(app)

# db migrate
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# Run Server
if __name__ == '__main__':
    manager.run()
