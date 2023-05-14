from cmtt.tasks import *

sentence = 'Bangladesh and Tripura India ko east side mai hain.'
pos = BiLSTM_NER()

lst = pos.getNERTags(sentence)
print(lst)

unks = pos.getUnks(sentence)
print(unks)
print()

sentence = 'India mai gully cricket chal raha hain yaha, right Soniya Gandhi?'

lst = pos.getNERTags(sentence)
print(lst)

unks = pos.getUnks(sentence)
print(unks)
print()