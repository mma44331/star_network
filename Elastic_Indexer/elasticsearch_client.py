



class ElasticsearchClient:
    def __init__(self,es_uri, index_name,logger):
        self.es_uri = es_uri
        self.index_name = index_name
        self.logger = logger
        self._create_indexer()

    def _create_indexer(self):
        try:
            if self.es_uri.indices.exists(index=self.index_name):
                self.logger.info(f"Index {self.index_name} already exists.")
                return
            mapping = {
                'mappings': {
                    'properties': {
                        'image_id': {'type': 'keyword'},
                        'meta_data': {
                            'properties': {
                                'size_bytes': {'type': 'long'},
                                'dimensions':{
                                    'properties': {
                                        'width': {'type': 'integer'},
                                        'height': {'type': 'integer'}
                                        }
                                    },
                                'format': {'type': 'keyword'}
                                }
                            },
                        'raw_text': {'type': 'text'},
                        'clean_text': {'type': 'text'},
                        'top_10': {'type': 'keyword'},
                        'list_of_weapons': {'type': 'keyword'},
                        'score_filling': {'type': 'keyword'}
                    }
                }
            }
            self.es_uri.indices.create(index=self.index_name, body=mapping)
            self.logger.info(f"Created index: {self.index_name}")
        except Exception as e:
            self.logger.error(f"Error creating index: {e}")

    def upsert(self,document, image_id):
        try:
            self.es_uri.update(index=self.index_name, id=image_id,doc=document,doc_as_upsert=True)

            self.logger.info(f"Upsert the image: {image_id} to elasticsearch")

        except Exception as e:
            self.logger.error(f"Failed to upsert {image_id}: {e}")

