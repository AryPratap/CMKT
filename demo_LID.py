from cmtt.tasks import HinglishToolKit

mytoolkit = HinglishToolKit()


BiLSTM = mytoolkit.XLM_HIEN_LID()
sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people choddega nhi, right?'

lst = BiLSTM.getLangTags(sentence)
print(lst)
print()

sentence = 'kya haal hai bhai! Let me get activated now aur fir khelthe hai?'
lst = BiLSTM.getLangTags(sentence)
print(lst)
print()

sentence = "Hey, how are you bhai? It has been kaafi lamba time since we last met."
lst = BiLSTM.getLangTags(sentence)
print(lst)
print()
