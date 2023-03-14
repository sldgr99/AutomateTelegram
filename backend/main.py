from app.factory import create_app
from app.db import initialize_db
import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join("connection.INI")))
app = create_app()
app.config['DEBUG'] = True
app.config['MONGODB_HOST'] = config['DEVELOPMENT']['DB_URI']
app.config['SECRET_KEY'] = 'greenduxlosuxaspix'
initialize_db(app)


def get_app():
    return app


if __name__ == "__main__":
    app.run(port=8000)