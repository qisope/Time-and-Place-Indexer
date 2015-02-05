from flask import Flask
from flask import Response
import json
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
            return self.success({'success': True})

        def delete_index():
            self.es_client.delete()
            return self.success({'success': True})

        self.app.add_url_rule('/mapping', 'create_index', create_index, methods=['POST'])
        self.app.add_url_rule('/mapping', 'delete_index', delete_index, methods=['DELETE'])

    def success(self, data):
        js = json.dumps(data)
        return Response(js, 200, mimetype='application/json')

    def run(self):
        self.app.run()
