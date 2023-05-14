from cmtt.tasks import HinglishToolKit


sentence = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people'

mytoolkit = HinglishToolKit()

pos = mytoolkit.BiLSTM_HINENG_POS()

lst = pos.getPOSTags(sentence)
print(lst)

unks = pos.getUnks(sentence)
print(unks)
print()

sentence = 'Na rahega bass na rahegi basuri.'

lst = pos.getPOSTags(sentence)
print(lst)

unks = pos.getUnks(sentence)
print(unks)
print()

sentence = 'tum kese ho. mei thik hu. Are you all right?'

lst = pos.getPOSTags(sentence)
print(lst)

unks = pos.getUnks(sentence)
print(unks)