from cmtt.preprocessing import *
print("\nCMTT Preprocessing Subpackage Demo (Porter Stemmer): ")
print()

english_text = "International conference myself happy agreed trying tractable bowled"
english_text_2 = "I am happy to have agreed to attend the international conference in computer science."

stemmer = PorterStemmer()
stemming = stemmer.stem("activate")
print(stemming)
print()

stemming = stemmer.stem(english_text_2)
print(stemming)
print()

hindi_text = "ख़रीदारों के लिए मार्ग दर्शिका"
hindi_stemmed = hindi_stem(hindi_text)
print(hindi_stemmed)
with open(r"test_hindi_stemmed.txt", 'w', encoding = "utf-8") as f:
  f.write(hindi_stemmed + "\n")

code_mixed_text = 'tu kesa hai mere bhai, kyuki I am fine. Empowerment toh people chaddange nhi, right?'
hien_stemmed = hien_stemmer(code_mixed_text)
hiennn = ' '.join(hien_stemmed)
print(hien_stemmed)
with open(r"test_hien_stemmed.txt", 'w', encoding = "utf-8") as f:
  f.write(hiennn + "\n")