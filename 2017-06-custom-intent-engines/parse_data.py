import pdb
import json
import numpy as np


def parseJson(file_pre, file_suf):
  file_pre = file_pre
  with open(file_pre + '/train_' + file_pre + file_suf + '.json', 'r') as f:
    json_data = json.load(f)
  datalist = json_data[file_pre]
  corr_data = []
  count = 0
  for dl in datalist:
    count += 1
    temp = {}
    temp['intent'] = file_pre
    data = dl['data']
    sent = []
    for t in data:
      sent.append(t['text'])
    temp['sent'] = ' '.join(sent)
    corr_data.append(temp)
  corr_data = np.array(corr_data)
  np.save(file_pre + '/train_' + file_pre + file_suf + '.npy', corr_data)
  print(count)


if __name__ == '__main__':
  file_pre = 'AddToPlaylist'
  file_suf = ''
  parseJson(file_pre, file_suf)