from cmtt.tasks import TaskToolKit

sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people'
mytoolkit = TaskToolKit("hineng")
pos = mytoolkit.pos(model_name="XLM Roberta base")

lst = pos.getPOSTags(sentence)
print(lst)
print()

sentence = 'Na rahega bass na rahegi basuri.'

lst = pos.getPOSTags(sentence)
print(lst)
print()

sentence = 'tum kese ho. mei thik hu. Are you all right?'

lst = pos.getPOSTags(sentence)
print(lst)
