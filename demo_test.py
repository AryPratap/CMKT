from cmtt.tasks import *
from cmtt.preprocessing import *
from cmtt.metrics import *
from cmtt.data import *

#mytoolkit = HinglishToolKit()

'''
code_mixed_text = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people chaddange nhi, right?'
hien_stemmed = hien_stemmer(code_mixed_text)
hiennn = ' '.join(hien_stemmed)
print(hien_stemmed)
with open(r"test_hien_stemmed.txt", 'w', encoding = "utf-8") as f:
  f.write(hiennn + "\n")
'''

sentence = "Deepak ji, channel ko kitna fund diya hai congress ne? 2006 me ameithi rape case kyu nahi discuss kiya kabhi?"
sentence = "RAHUL jab dieting par hota hai toh green tea peeta hai."
#sentence = "Deepak ji, channel ko kitna fund diya hai congress ne? 2006 me ameithi rape case kyu nahi discuss kiya kabhi?"
#sentence = "4 din me 2 accidents, kuch to jhol hai, shayad politics ho rahi hai.."
#sentence = "The ultimate twist Dulhan dandanate huye brings Baraat .... Dulha"
#sentence = "laufed ... first u hav to correct ur english baad me sochna use !!!"
#lid = mytoolkit.XLM_HIEN_LID()
#print(lid.getLangTags(sentence))

#ner = mytoolkit.XLM_HIEN_NER()
#print(ner.getNERTags(sentence))
#print(burstiness(sentence))



#ner = mytoolkit.XLM_HIEN_NER()

#pos = mytoolkit.XLM_HIEN_POS()
#print(pos.getPOSTags("Aap kaise hai main thik. I am good. My name is Ramesh"))

# List CMTT datasets for the task of LID
# print("List CMTT Datasets Function (search_key = task, search_term = ner): ")
# data = ListDatasets(search_key="task", search_term = "ner", isPrint=True,details=True)
# print()
# # List CMTT datasets for hineng language
# print("List CMTT Datasets Function (search_key = language, search_term = hineng): ")
# data1 = ListDatasets(search_key="language", search_term = "hineng", isPrint=True, details=True)
# mytoolkit = TaskToolKit(lang="hineng")
# lid = mytoolkit.lid(model_name="XLM ")

# print(lid.getLangTags(sentence))


tokenizer = Tokenizers("en")


print(tokenizer.word_tokenize(sentence))
