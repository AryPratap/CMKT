from cmtt.tasks import HinglishToolKit

mytoolkit = HinglishToolKit()

ner = mytoolkit.XLM_HIEN_NER()

print(ner.getNERTags("Aap kaise hai main thik. I am good. My name is Ramesh"))