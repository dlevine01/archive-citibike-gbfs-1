This repo pulls station information and station status data from citibike [gbfs feed](http://gbfs.citibikenyc.com/gbfs/gbfs.json) every fifteen minutes and saves the raw json files in the [/data](/data) folder. 

Files are labeled with their Unix time taken from `last_updated` timestamp in the gbfs data. 

e.g. [1685068015_stations.json](data/1685068015_stations.json) is the `station_information` data pulled at 1685068015 (i.e. May 25 2023 22:26:55 GMT-0400 (Eastern Daylight Time));  [1685068015_status.json](data/1685068015_status.json) is the `station_status` pulled at 1685068015
