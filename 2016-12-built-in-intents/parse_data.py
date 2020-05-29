import pdb
import json
import numpy as np

file = 'benchmark_data.json'
with open(file, 'r') as f:
  json_data = json.load(f)
print(json_data.keys())  # ['domains', 'version']
domains = json_data['domains']
print('domain length', len(domains))

corr_data = []
for domain in domains:
  temp = {}
  temp['long_description'] = domain['description']
  temp['short_description'] = domain['name']
  intents = domain['intents']
  print('intent length', len(intents))
  for intent in intents:
    temp['intent'] = intent['name']
    queries = intent['queries']
    print('query length', len(queries))
    for query in queries:
      temp['query'] = query['text']
      corr_data.append(temp)

print(len(corr_data))
corr_data = np.array(corr_data)
np.save('benchmark_data.npy', corr_data)
"""
(Pdb) json_data['domains'][3]['intents'][0].keys()
dict_keys(['description', 'benchmark', 'queries', 'slots', '@type', 'name'])

len(json_data['domains'][3]['intents'][0]['description'])



json_data['domains'][3]['intents'][0]['queries'] 
# length
(Pdb) json_data['domains'][3]['intents'][0]['queries'][0].keys()
dict_keys(['text', 'results_per_service'])
json_data['domains'][3]['intents'][0]['queries'][0]['text']





print(domains.keys())  # ['description', '@type', 'intents', 'name']
"Queries that are related to places (restaurants, shops, concert halls, etc), as well as to the user's location."
'Queries that are related to reservation.'
'Queries that are related to transit and navigation.'
'Queries that relate to weather.'

(Pdb) json_data['domains'][3]['name']
'weather'
(Pdb) json_data['domains'][2]['name']
'transit'
(Pdb) json_data['domains'][1]['name']
'reservation'
(Pdb) json_data['domains'][0]['name']
'places'

print(len(domains))  # 4



(Pdb) len(json_data['domains'][0]['intents'])
4
(Pdb) len(json_data['domains'][1]['intents'])
2
(Pdb) len(json_data['domains'][2]['intents'])
3
(Pdb) len(json_data['domains'][3]['intents'])
1
"""
