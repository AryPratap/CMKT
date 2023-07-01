from cmkt.preprocessing import *

print("\nCMKT Preprocessing Subpackage Demo (Sentence Piece Tokenizer): ")
print()

'''
Language convention:
'en' -> English
'hi' -> Hindi
'hineng' -> Hinglish
'''

# Sentence piece based Tokenizer for English
_en = " This is a sentence-piece based tokenizer, supporting the english language."
Spm_en = SentencepieceTokenizer('en')
lst = Spm_en.tokenize(_en)
with open(r"test_en.txt", 'w', encoding = "utf-8") as f:
  for i in lst:
    f.write(i + "\n")

# Sentence piece based Tokenizer for Hindi
_hi = " मैं इनदोनों श्रेणियों के बीच कुछ भी० सामान्य नहीं देखता।"
Spm_hi = SentencepieceTokenizer('hi')
lst = Spm_hi.tokenize(_hi)
with open(r"test_hi.txt", 'w', encoding = "utf-8") as f:
  for i in lst:
    f.write(i + "\n")



# Sentence piece based Tokenizer for Devnagari Hindi and Roman English Mixed Text
_hinDev_engRom = " कैसे हो मित्र इनदोनों? Aur batao, I am good."
Spm_hien = SentencepieceTokenizer('hineng')
lst = Spm_hien.tokenize(_hinDev_engRom)
with open(r"test_hinDev_engRom.txt", 'w', encoding = "utf-8") as f:
  for i in lst:
    f.write(i + "\n")

# Sentence Piece detokenizer
path = os.path.dirname(os.path.realpath(__file__))
f = open(os.path.join(path, "test_hien.txt"), encoding = "utf-8")
tokens = []
with f as reader:
  while True:
    token = reader.readline()
    if not token:
      break
    token = token.strip()
    tokens.append(token)

# print(tokens)
detokenized_text = Spm_hien.detokenize(tokens)
print("Sentencepiece DeTokenizer: \n", detokenized_text)