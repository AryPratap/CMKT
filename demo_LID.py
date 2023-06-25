from cmkt.tasks import TaskToolKit

mytoolkit = TaskToolKit("hineng")


lid = mytoolkit.lid(model_name="XLM Roberta base")
sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people choddega nhi, right?'

lst = lid.getLangTags(sentence)
print(lst)
print()

sentence = 'kya haal hai bhai! Let me get activated now aur fir khelthe hai?'
lst = lid.getLangTags(sentence)
print(lst)
print()

sentence = "Hey, how are you bhai? It has been kaafi lamba time since we last met."
lst = lid.getLangTags(sentence)
print(lst)
print()
