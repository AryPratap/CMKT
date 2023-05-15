from cmtt.tasks import HinglishToolKit

mytoolkit = HinglishToolKit()


BiLSTM = mytoolkit.BiLSTM_HINENG_LID()
sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people choddega nhi, right?'

lst = BiLSTM.getLangTags(sentence)
print(lst)
unks = BiLSTM.getUnks(sentence)
print(unks)
print()

sentence = 'kya haal hai bhai! Let me get activated now aur fir khelthe hai?'
lst = BiLSTM.getLangTags(sentence)
print(lst)
unks = BiLSTM.getUnks(sentence)
print(unks)

sentence = "Hey, how are you bhai? It has been kaafi lamba time since we last met."
lst = BiLSTM.getLangTags(sentence)
print(lst)
unks = BiLSTM.getUnks(sentence)
print(unks) 
