from cmtt.preprocessing import RomanDevanagariTokenizer, RomanTokenizer, devanagariTokenizer


## Tokenizing english Text 
english_tokenizer = RomanTokenizer()

eng_sent = "I think you have not prepared well, you got only 67%, but I got 9.6 GPA. Understood ?"

#sentence tokenization
print(english_tokenizer.sent_tokenize(eng_sent))
print()

# Word Tokenization
print(english_tokenizer.word_tokenize(eng_sent))
print()

## Tokenizing devanagari Text 
hindi_tokenizer = devanagariTokenizer()

hin_sent = "मैं अपने दोस्त से मिलने जा रहा हूँ। आज मैंने अपना खाना बनाया॥ आप कैसे हैं:?"

# Sentence tokenization 
print(hindi_tokenizer.sent_tokenize(hin_sent))
print()

# Word Tokenization
print(hindi_tokenizer.word_tokenize(hin_sent))
print()

## Tokenizing Roman Devanagari mixed script text 
mixed_tokenizer = RomanDevanagariTokenizer()

mix_sent = "I think you have not prepared well. आज मैंने अपना खाना बनाया॥ आप कैसे हैं:? I got 9.6 GPA. Understood?"

# Sentence tokenization 
print(mixed_tokenizer.sent_tokenize(mix_sent))
print()

# Word tokenization 
print(mixed_tokenizer.word_tokenize(mix_sent))
print()


