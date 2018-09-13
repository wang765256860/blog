import os
from flask_migrate import Migrate
from dotenv import load_dotenv
from app import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
