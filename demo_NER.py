from cmtt.tasks import HinglishToolKit

sentence = 'Bangladesh and Tripura India ko east side mai hain.'
mytoolkit = HinglishToolKit()

ner = mytoolkit.BiLSTM_HINENG_NER()

lst = ner.getNERTags(sentence)
print(lst)

unks = ner.getUnks(sentence)
print(unks)
print()

sentence = 'India mai gully cricket chal raha hain yaha, right Soniya Gandhi?'

lst = ner.getNERTags(sentence)
print(lst)

unks = ner.getUnks(sentence)
print(unks)
print()