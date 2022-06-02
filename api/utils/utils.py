import json

def parse_json(data):
    json_data = (data).decode('utf-8').replace("'", '"')
    return json.loads(json_data)