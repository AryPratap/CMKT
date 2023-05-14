from cmtt.preprocessing import *
print("\nCMTT Preprocessing Subpackage Demo")
print()

# Tokenizers
# text = "This Python interpreter is in a conda environment, but the environment has not been activated.  Libraries may fail to load.  To activate this environment"
text = "Hello world! This a python code. Adding random words activate code decrease wastage."
WhitespaceT = WhitespaceTokenizer()
tokenized_text_whitespace = WhitespaceT.tokenize(text)
print("Whitespace Tokenizer: \n", tokenized_text_whitespace)
print(len(tokenized_text_whitespace))
print()

# Word Tokenizer
WordT = WordTokenizer(do_lower_case=False)
tokenized_text_word = WordT.tokenize(text)
print("Word Tokenizer: \n", tokenized_text_word)
print(len(tokenized_text_word))
print()

# Wordpiece Tokenizer
WordpieceT = Wordpiece_tokenizer()
tokenized_text_wordpiece  = WordpieceT.tokenize(text)
print("Wordpiece Tokenizer: \n", tokenized_text_wordpiece)
print(len(tokenized_text_wordpiece))
print()

# Devanagari Tokenizer
devanagari_text = "मैं इनदोनों श्रेणियों के बीच कुछ भी० सामान्य नहीं देखता। मैं कुछ नहीं, ट ट॥"
DevanagariT = DevanagariTokenizer()
tokenized_text_devanagari_words  = DevanagariT.word_tokenize(devanagari_text)
print("Devanagari Tokenizer: \n", tokenized_text_devanagari_words)
print(len(tokenized_text_devanagari_words))
print()

tokenized_text_devanagari_characters  = DevanagariT.character_tokenize(devanagari_text)
print("Devanagari Character Tokenizer: \n", tokenized_text_devanagari_characters)
print(len(tokenized_text_devanagari_characters))
print()

# DeTokenizers
whitespace_text = WhitespaceT.detokenize(tokenized_text_whitespace)
print("Whitespace DeTokenizer: \n", whitespace_text)
print()

word_text = WordT.detokenize(tokenized_text_word)
print("Word DeTokenizer: \n", word_text)
print()

wordpiece_text = WordpieceT.detokenize(tokenized_text_wordpiece)
print("Wordpiece DeTokenizer: \n", wordpiece_text)
print()

devanagari_text = DevanagariT.word_detokenize(tokenized_text_devanagari_words)
print("Devanagari DeTokenizer: \n", devanagari_text)
print()

# Search function
instances, list_instances = search_word(text, 'this', tokenize = True, width = 3)
print()