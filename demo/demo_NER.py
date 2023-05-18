from cmtt.tasks import HinglishToolKit

sentence = 'Bangladesh and Tripura India ko east side mai hain.'
mytoolkit = HinglishToolKit()

ner = mytoolkit.XLM_HIEN_NER()

lst = ner.getNERTags(sentence)
print(lst)
print()

sentence = 'India mai gully cricket chal raha hain yaha, right Soniya Gandhi?'

lst = ner.getNERTags(sentence)
print(lst)

