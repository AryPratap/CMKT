from cmkt.tasks import TaskToolKit

sentence = 'Bangladesh and Tripura India ko east side mai hain.'
mytoolkit = TaskToolKit("hineng")

ner = mytoolkit.ner(model_name="XLM Roberta base")

lst = ner.getNERTags(sentence)
print(lst)
print()

sentence = 'India mai gully cricket chal raha hain yaha, right Soniya Gandhi?'

lst = ner.getNERTags(sentence)
print(lst)

