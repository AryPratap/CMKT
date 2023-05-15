from cmtt.tasks import HinglishToolKit

mytoolkit = HinglishToolKit()

#ner = mytoolkit.XLM_HIEN_NER()

pos = mytoolkit.XLM_HIEN_POS()
print(pos.getPOSTags("Aap kaise hai main thik. I am good. My name is Ramesh"))