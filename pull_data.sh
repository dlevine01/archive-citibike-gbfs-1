curl 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json' -o 'data/temp_stations.json'
curl 'https://gbfs.citibikenyc.com/gbfs/en/station_status.json' -o 'data/temp_status.json'

echo "✔downloaded data"

timestamp=$(jq -r '.last_updated' 'data/temp_status.json')

echo "timestamp: $timestamp"

mv 'data/temp_stations.json' "data/${timestamp}_stations.json"
mv 'data/temp_status.json' "data/${timestamp}_status.json"

echo "✔relabeled"