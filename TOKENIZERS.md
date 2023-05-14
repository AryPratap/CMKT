# CMTT Tokenizers
Tokenization is the process of converting natural language text into a sequence of tokens that can be considered as discrete elements. It is the first step in any NLP pipeline. Tokenization can separate sentences, words, characters, or subwords. 

## Rule Based Tokenization
### White Space Tokenization
  It is the simplest way to tokenize natural language text. Here whitespace within the text is used as the delimiter of words.

  ```Python
    from cmtt.preprocessing import *
    text = "Hello world! This a python code. Let's activate"
    tokenized_text_whitespace = whitespace_tokenize(text)
    print("Whitespace Tokenizer: ", tokenized_text_whitespace)
    # Output => Whitespace Tokenizer: ['Hello', 'world!', 'This', 'a', 'python', 'code.', "Let's", 'activate']
  ```

### Word Tokenization
  In this method, the text is split into tokens based on both whitespaces and punctuations. 
  ```Python
    from cmtt.preprocessing import *
    text = "Hello world! This a python code. Let's activate"
    WordT = WordTokenizer()
    tokenized_text_word = WordT.tokenize(text)
    print("Word Tokenizer: ", tokenized_text_word)
    # Output => Word Tokenizer: ['hello', 'world', '!', 'this', 'a', 'python', 'code', '.', 'let', "'", 's', 'activate']
  ```

## Subword Tokenization
Subword tokenization algorithms rely on the principle that frequently used words should not be split into smaller subwords, but rare words should be decomposed into meaningful subwords. Subword tokenization can help us in handling Unknown words in a test dataset.

"##" symbol means that the rest of the token should be attached to the previous one, without space (for decoding or reversal of the tokenization).

"[Unk]" symbol means unknown or not present in the base vocabulary.

### WordPiece Tokenizer
  WordPiece is the subword tokenization algorithm used for BERT, DistilBERT, and Electra.
  WordPiece first initializes the vocabulary to include every character present in the training data and progressively learns a given number of merge rules. WordPiece does not choose the most frequent symbol pair, but the one that maximizes the likelihood of the training data once added to the vocabulary.

  ```Python
    from cmtt.preprocessing import *
    text = "Hello world! This a python code. Let's activate"
    WordpieceT= Wordpiece_tokenizer()
    tokenized_text_wordpiece  = WordpieceT.tokenize(text)
    print("Wordpiece Tokenizer: ", tokenized_text_wordpiece)
    # Output => Wordpiece Tokenizer: ['[UNK]', 'world', '!', '[UNK]', 'a', 'py', '##th', '##on', 'code', '.', '[UNK]', "'", 's', 'activ', '##ate']
  ```

### SentencePiece Tokenizer
  Sentencepiece Tokenizer is a language independent subword tokenizer that replaces whitespace in the text, if any, with the the "▁" character, followed by using either the Byte Pair Encoding or the Unigram algorithm to construct the volcublary.

  ```Python
  from cmtt.preprocessing import *
  text = "Hello world! This a python code. Let's activate"
  SentencepieceT = Sentencepiece_tokenizer('en')
  tokenized_text_sentencepiece = SentencepieceT.tokenize(text)
  with open(r"tokens.txt", 'w', encoding = "utf-8") as f:
    for i in tokenized_text_sentencepiece:
      f.write(i + "\n")
  # Output => "▁Hello", "▁world", "!", "▁This", "▁a", "▁py", "thon", "▁code", ".", "▁Let", "'", "s", "▁activate"
  ```