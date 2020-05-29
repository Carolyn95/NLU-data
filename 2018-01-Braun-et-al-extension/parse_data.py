import pdb
import json
import numpy as np


# sentences -> text, intent
def parseJson(file_pre, file_suf):
  file_pre = file_pre
  with open(file_pre + file_suf + '.json', 'r') as f:
    json_data = json.load(f)

  sentences = json_data['sentences']
  # pdb.set_trace()
  # print()
  corr_data = []
  count = 0
  for sent in sentences:
    count += 1
    temp = {}
    temp['intent'] = sent['intent']
    temp['sent'] = sent['text']
    corr_data.append(temp)
  corr_data = np.array(corr_data)
  np.save(file_pre + file_suf + '.npy', corr_data)
  print(count)


if __name__ == '__main__':
  file_pre = 'WebApplicationsCorpus'  # 'AskUbuntuCorpus', 'ChatbotCorpus', 'WebApplicationsCorpus'
  file_suf = ''
  parseJson(file_pre, file_suf)