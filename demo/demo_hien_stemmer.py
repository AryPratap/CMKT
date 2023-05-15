from cmtt.preprocessing import *


code_mixed_text = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people chaddange nhi, right?'
hien_stemmed = hien_stemmer(code_mixed_text)
hiennn = ' '.join(hien_stemmed)
print(hien_stemmed)
with open(r"test_hien_stemmed.txt", 'w', encoding = "utf-8") as f:
  f.write(hiennn + "\n")
