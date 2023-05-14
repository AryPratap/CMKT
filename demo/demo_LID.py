from cmtt.tasks import *

lid = BiLSTM_LID()
sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people choddega nhi, right?'
lst = lid.getLangTags(sentence)
print(lst)
unks = lid.getUnks(sentence)
print(unks)
print()

sentence = 'kya haal hai bhai! Let me get activated now aur fir khelthe hai?'
lst = lid.getLangTags(sentence)
print(lst)
unks = lid.getUnks(sentence)
print(unks)

sentence = "Hey, how are you bhai? It has been kaafi lamba time since we last met."
lst = lid.getLangTags(sentence)
print(lst)
unks = lid.getUnks(sentence)
print(unks)