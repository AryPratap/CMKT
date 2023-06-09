from cmtt.preprocessing import *
print("\nCMTT Preprocessing Subpackage Demo (Porter Stemmer): ")
print()

english_text = "International conference myself happy agreed trying tractable bowled"
english_text_2 = "I am happy to have agreed to attend the international conference in computer science."

en_stemmer = Stemmer('en')
stemming = en_stemmer.stem("activate")
print(stemming)
print()

stemming = en_stemmer.stem(english_text_2)
print(stemming)
print()


hi_stemmer = Stemmer('hi')
hindi_text = "ख़रीदारों के लिए मार्ग दर्शिका"   
hindi_stemmed = hi_stemmer.stem(hindi_text)
print(hindi_stemmed)
# with open(r"test_hindi_stemmed.txt", 'w', encoding = "utf-8") as f:
#   f.write(hindi_stemmed + "\n")

