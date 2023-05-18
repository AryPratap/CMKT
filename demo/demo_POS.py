from cmtt.tasks import HinglishToolKit

sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people'
mytoolkit = HinglishToolKit()
pos = mytoolkit.XLM_HIEN_POS()

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
