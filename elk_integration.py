from elasticsearch import Elasticsearch

def send_to_elk(packet_data):
    es = Elasticsearch()
    es.index(index="honeypot_guard", doc_type="packet", body=packet_data)
