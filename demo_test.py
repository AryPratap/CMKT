from cmtt.tasks import HinglishToolKit
from cmtt.preprocessing import hien_stemmer

mytoolkit = HinglishToolKit()


code_mixed_text = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people chaddange nhi, right?'
hien_stemmed = hien_stemmer(code_mixed_text)
hiennn = ' '.join(hien_stemmed)
print(hien_stemmed)
with open(r"test_hien_stemmed.txt", 'w', encoding = "utf-8") as f:
  f.write(hiennn + "\n")

#ner = mytoolkit.XLM_HIEN_NER()

#pos = mytoolkit.XLM_HIEN_POS()
#print(pos.getPOSTags("Aap kaise hai main thik. I am good. My name is Ramesh"))

