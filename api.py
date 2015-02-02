from flask import Flask
from management.elasticsearch import ElasticsearchManagement


class Api:
    def __init__(self, config):
        app = Flask(__name__)
        app.debug = True

        self.app = app
        self.es_client = ElasticsearchManagement(config)

        self.create_routes()

    def create_routes(self):
        def create_index():
            self.es_client.create()
            return {'success': True}

        self.app.add_url_rule('/mapping', 'create_index', create_index)

    def run(self):
        self.app.run()
