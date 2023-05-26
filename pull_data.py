import json,requests
stations_get = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_information.json')
status_get = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
status_json = status_get.json()
timestamp = status_json['last_updated']
with open(f"data/{timestamp}_stations.json", 'w') as stations_file:
    json.dump(stations_get.json(), stations_file)
with open(f"data/{timestamp}_status.json", 'w') as status_file:
    json.dump(status_json, status_file)