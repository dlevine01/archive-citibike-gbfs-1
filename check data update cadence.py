import time
import requests
import hashlib
import math
import pandas as pd

#---
# this json hash funciton
"""
(C) Oliver Schoenborn
License: modified MIT, ie MIT plus the following restriction: This code 
can be included in your code base only as the complete file, and this 
license comment cannot be removed or changed. This code was taken from 
https://github.com/schollii/sandals/blob/master/json_sem_hash.py. If you 
find modifications necessary, please contribute a PR so that the open-source
community can benefit the same way you benefit from this file.
GIT_COMMIT: 05-26-2023
"""


from typing import Union, Dict, List
import hashlib

JsonType = Union[str, int, float, List['JsonType'], 'JsonTree']
JsonTree = Dict[str, JsonType]
StrTreeType = Union[str, List['StrTreeType'], 'StrTree']
StrTree = Dict[str, StrTreeType]


def sorted_dict_str(data: JsonType) -> StrTreeType:
    if type(data) == dict:
        return {k: sorted_dict_str(data[k]) for k in sorted(data.keys())}
    elif type(data) == list:
        return [sorted_dict_str(val) for val in data]
    else:
        return str(data)


def get_json_sem_hash(data: JsonTree, hasher=hashlib.sha256) -> str:
    return hasher(bytes(repr(sorted_dict_str(data)), 'UTF-8')).hexdigest()

#---

results_list = []

for its in range(10000):

    get_time = math.floor(time.time())

    r = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')

    last_updated = r.json()['last_updated']
    ttl = r.json()['ttl']
    data_hash = get_json_sem_hash(r.json()['data'])

    results_list.append((get_time, last_updated, ttl, data_hash))

    time.sleep(0.5)

results = pd.DataFrame(
    data=results_list,
    columns=['get_time','last_update','ttl','data_hash']
)

results['get_time'] = pd.to_datetime(results['get_time'],unit='s')

changes_last_update = results[results['last_update'].diff() != 0]

changes_last_update = changes_last_update.iloc[1:-1]

print('mean time to last_update change:')
print(changes_last_update['get_time'].diff().mean())

changes_data = results[results['data_hash'] != results.shift(-1)['data_hash']]

changes_data = changes_data.iloc[1:-1]

print('mean time to last_update change:')
print(changes_data['get_time'].diff().mean())

