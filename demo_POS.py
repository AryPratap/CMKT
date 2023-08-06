from cmkt.tasks import TaskToolKit

sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people'
mytoolkit = TaskToolKit("hineng")
pos = mytoolkit.pos(model_name="xlm-roberta-base")

lst = pos.get_predictions(sentence)
print(lst)
print()

sentence = 'Na rahega bass na rahegi basuri.'

lst = pos.get_predictions(sentence)
print(lst)
print()

sentence = 'tum kese ho. mei thik hu. Are you all right?'

lst = pos.get_predictions(sentence)
print(lst)

sentence = "Rahul apni nayi car se aaj ek long drive par gya."
print(pos.get_predictions(sentence))