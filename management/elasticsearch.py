from elasticsearch.client import Elasticsearch

class ElasticsearchManagement:
    def __init__(self, config):
        self.index = config['elasticsearch_index']
        self.type = config['elasticsearch_type']

        host = config['elasticsearch_host']
        self.client = Elasticsearch(hosts=[host])

    def create(self):
        body = self.get_index_body()
        self.client.indices.create(index=self.index, body=body)

    def get_index_body(self):
        return {
            'settings': {},
            'mappings': {
                self.type: {
                    'properties': {

                    }
                }
            }
        }