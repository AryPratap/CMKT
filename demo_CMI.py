from cmtt.tasks import *
from cmtt.metrics import *

lid = BiLSTM_LID()
sentence = 'mei insaan hu'
lst = lid.getLangTags(sentence)
print(lst)

tag_sent = ""
for i in lst:
  tag_sent += i[1] + " "

tag_sent = tag_sent.strip()
print(tag_sent)

Cu = utteranceCMI(tag_sent)
print(Cu)

Cmi = cmi(tag_sent)
print(Cmi)