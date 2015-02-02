import os
import configparser

from api import Api

config = configparser.ConfigParser()
config.read('config.ini')

activeConfigName = os.environ['PYTHON_ENV']
activeConfig = config[activeConfigName]

api = Api(activeConfig)
api.run()