import unicodedata
import os
import re
from urllib.request import urlopen
import pickle
import warnings

def convert_to_unicode(text):
  """Converts `text` to Unicode (if it's not already), assuming utf-8 input."""
  if isinstance(text, str):
    return text
  elif isinstance(text, bytes):
    return text.decode("utf-8", "ignore")
  else:
    raise ValueError("Unsupported string type: %s" % (type(text)))

##################################################
# Whitespace Tokenizer
##################################################
class WhitespaceTokenizer(object):
  def tokenize(self, text):
    text = text.strip()
    if not text:
      return []
    tokens = text.split()
    return tokens

  def detokenize(self, tokens):
    if type(tokens) is list:
      return ' '.join(tokens)
    else:
      raise TypeError('Tokens needs to be of type list. Expected type list but got type ' + str(type(tokens)))

##################################################
# Word Tokenizer
##################################################
class WordTokenizer(object):
  """Runs basic tokenization (punctuation splitting, lower casing, etc.)."""

  def __init__(self, do_lower_case=True):
    """Constructs a BasicTokenizer.
    Args:
      do_lower_case: Whether to lower case the input.
    """
    self.do_lower_case = do_lower_case

  def tokenize(self, text):
    """Tokenizes a piece of text."""
    text = convert_to_unicode(text)
    text = self._clean_text(text)

    WhitespaceT = WhitespaceTokenizer()
    orig_tokens = WhitespaceT.tokenize(text)
    split_tokens = []
    for token in orig_tokens:
      if self.do_lower_case:
        token = token.lower()
        token = self._run_strip_accents(token)
      split_tokens.extend(self._run_split_on_punc(token))

    output_tokens = WhitespaceT.tokenize(" ".join(split_tokens))
    return output_tokens

  def detokenize(self, tokens):
    if type(tokens) is list:
      text = ""
      for i in tokens:
        if len(i) == 1:
          if self._is_punctuation(i):
            text += i
          else:
            text += " " + i
        else:
          text += " " + i
      return text.strip()    
    else:
      raise TypeError('Tokens needs to be of type list. Expected type list but got type ' + str(type(tokens)))

  def _run_strip_accents(self, text):
    """Strips accents from a piece of text."""
    text = unicodedata.normalize("NFD", text)
    output = []
    for char in text:
      cat = unicodedata.category(char)
      if cat == "Mn":
        continue
      output.append(char)
    return "".join(output)

  def _run_split_on_punc(self, text):
    """Splits punctuation on a piece of text."""
    chars = list(text)
    i = 0
    start_new_word = True
    output = []
    while i < len(chars):
      char = chars[i]
      if self._is_punctuation(char):
        output.append([char])
        start_new_word = True
      else:
        if start_new_word:
          output.append([])
        start_new_word = False
        output[-1].append(char)
      i += 1

    return ["".join(x) for x in output]

  def _clean_text(self, text):
    """Performs invalid character removal and whitespace cleanup on text."""
    output = []
    for char in text:
      cp = ord(char)
      if cp == 0 or cp == 0xfffd or self._is_control(char):
        continue
      if self._is_whitespace(char):
        output.append(" ")
      else:
        output.append(char)
    return "".join(output)

  def _is_whitespace(self, char):
    """Checks whether `chars` is a whitespace character."""
    # \t, \n, and \r are technically contorl characters but we treat them
    # as whitespace since they are generally considered as such.
    if char == " " or char == "\t" or char == "\n" or char == "\r":
      return True
    cat = unicodedata.category(char)
    if cat == "Zs":
      return True
    return False

  def _is_control(self, char):
    """Checks whether `chars` is a control character."""
    # These are technically control characters but we count them as whitespace
    # characters.
    if char == "\t" or char == "\n" or char == "\r":
      return False
    cat = unicodedata.category(char)
    if cat in ("Cc", "Cf"):
      return True
    return False

  def _is_punctuation(self, char):
    """Checks whether `chars` is a punctuation character."""
    cp = ord(char)
    # We treat all non-letter/number ASCII as punctuation.
    # Characters such as "^", "$", and "`" are not in the Unicode
    # Punctuation class but we treat them as punctuation anyways, for
    # consistency.
    if ((cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or
        (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126)):
      return True
    cat = unicodedata.category(char)
    if cat.startswith("P"):
      return True
    return False

##################################################
# Wordpiece Tokenizer
##################################################
def load_vocab_list():
  """Loads a vocabulary file into a dictionary."""
  vocab = []
  path = os.path.dirname(os.path.realpath(__file__))
  f = open(os.path.join(path, "vocab_2.txt"), 'r')
 
  with f as reader:
    while True:
      token = convert_to_unicode(reader.readline())
      if not token:
        break
      token = token.strip()
      vocab.append(token)
  return vocab 

class Wordpiece_tokenizer(object):
  def __init__(self, vocab = load_vocab_list()):
    self.vocab = vocab

  def encode_word(self, word):
    tokens = []
    while len(word) > 0:
      i = len(word)
      while i > 0 and word[:i].lower() not in self.vocab:
        i -= 1
      if i == 0:
        return ["[UNK]"]
      tokens.append(word[:i])
      word = word[i:]
      if len(word) > 0:
        word = f"##{word}"
    return tokens

  def tokenize(self, text):
    """
      Tokenizes a piece of text into its word pieces.
      For example:
        input = "unaffable"
        output = ["un", "##aff", "##able"]
      Args:
        text: A single token or whitespace separated tokens. This should have already been passed through `BasicTokenizer.
      Returns:
        A list of wordpiece tokens.
    """
    text = text.strip()
    text = re.findall(r"[\w]+|[^\s\w]", text)
    encoded_words = [self.encode_word(word) for word in text]
    return sum(encoded_words, [])

  def detokenize(self, tokens):
    if type(tokens) is list:
      text = ""
      for i in tokens:
        if len(i) == 1:
          if self._is_punctuation(i):
            text += i
          else:
            text += " " + i
        elif "##" in i:
          text += i[2:]
        else:
          text += " " + i
      return text.strip()    
    else:
      raise TypeError('Tokens needs to be of type list. Expected type list but got type ' + str(type(tokens)))

  def _is_punctuation(self, char):
    """Checks whether `chars` is a punctuation character."""
    cp = ord(char)
    # We treat all non-letter/number ASCII as punctuation.
    # Characters such as "^", "$", and "`" are not in the Unicode
    # Punctuation class but we treat them as punctuation anyways, for
    # consistency.
    if ((cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or
        (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126)):
      return True
    cat = unicodedata.category(char)
    if cat.startswith("P"):
      return True
    return False

##################################################
# Devanagari Tokenizer
##################################################
class DevanagariTokenizer(object):
  def word_tokenize(self, text):
    text = text.strip()
    processed_text = ""
    for i in text:
      if self._is_punctuation(i):
        processed_text += " " + i
      else:
        processed_text += i
    
    tokens = processed_text.split(" ")
    return tokens        

  def character_tokenize(self, text):
    text = text.strip()
    if not text:
      return []
    tokens = re.findall(r"[\w]+|[^\s\w]", text)
    return tokens

  def word_detokenize(self, tokens):
    if type(tokens) is list:
      text = ""
      for i in tokens:
        if len(i) == 1:
          if self._is_punctuation(i):
            text += i
          else:
            text += " " + i
        else:
          text += " " + i
      return text.strip()   
    else:
      raise TypeError('Tokens needs to be of type list. Expected type list but got type ' + str(type(tokens)))

  def _is_punctuation(self, char):
    """Checks whether `chars` is a punctuation character."""
    cp = ord(char)
    # We treat all non-letter/number ASCII as punctuation.
    # Characters such as "^", "$", and "`" are not in the Unicode
    # Punctuation class but we treat them as punctuation anyways, for
    # consistency.
    if ((cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or
        (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126)):
      return True
    cat = unicodedata.category(char)
    if cat.startswith("P"):
      return True
    return False
  
### New tokenizers 

# Roman Tokenizers 
class RomanTokenizer():
    """
    Tokinzer for text in roman script. It includes word tokenizer, sentence tokenizer and single sentence word tokenizer. 
    """
    def __init__(self):

    # Starting quotes.
        self.start_quotations = [
            (re.compile("([«“‘„]|[`]+)", re.U), r" \1 "),
            (re.compile(r"^\""), r"``"),
            (re.compile(r"(``)"), r" \1 "),
            (re.compile(r"([ \(\[{<])(\"|\'{2})"), r"\1 `` "),
            (re.compile(r"(?i)(\')(?!re|ve|ll|m|t|s|d|n)(\w)\b", re.U), r"\1 \2"), # To deal with can't to "can" and "'t". 
        ]

        # Ending quotes.
        self.end_quotations = [
            (re.compile("([»”’])", re.U), r" \1 "),
            (re.compile(r"''"), " '' "),
            (re.compile(r'"'), " '' "),
            (re.compile(r"([^' ])('[sS]|'[mM]|'[dD]|') "), r"\1 \2 "),
            (re.compile(r"([^' ])('ll|'LL|'re|'RE|'ve|'VE|n't|N'T) "), r"\1 \2 "), # to deal with they'll aren't etc. 
        ]

        # Punctuation.
        self.punctuation = [
            (re.compile(r'([^\.])(\.)([\]\)}>"\'' "»”’ " r"]*)\s*$", re.U), r"\1 \2 \3 "), #This pattern matches a period that is not at the end of a sentence
                                                                                            # adds space before and after period.

            (re.compile(r"([:,])([^\d])"), r" \1 \2"),#This pattern matches any colon or comma that is not followed by a digit
                                                    #and adds spaces before and after it.

            (re.compile(r"([:,])$"), r" \1 "),#This pattern matches any colon or comma that is at the end of a sentence, and adds a space before it.

            (
                re.compile(r"\.{2,}", re.U), #This pattern matches two or more consecutive periods (i.e., ellipses) 
                r" \g<0> ",                  #and adds spaces before and after them.
            ),  

            (re.compile(r"[;@#$%&]"), r" \g<0> "), # This pattern matches any of the specified punctuation characters 
                                                #and adds spaces before and after them.
            (                                      
                re.compile(r'([^\.])(\.)([\]\)}>"\']*)\s*$'), #This pattern handles the final period in a text, matching any period that is at the end of a sentence and adding a space before it. 
                r"\1 \2\3 ",                                  #It also captures any punctuation that follows the period and adds it back in after the space
            ),  # Handles the final period.

            (re.compile(r"[?!]"), r" \g<0> "), #his pattern matches any exclamation point or question mark and adds spaces before and after it.

            (re.compile(r"([^'])' "), r"\1 ' "), #This pattern matches any single quote that is not preceded by 
                                                #another single quote (which would indicate a contraction) and adds a space before and after it.
            (                                    
                re.compile(r"[*]", re.U), #This pattern matches any asterisk and adds spaces before and after it.
                r" \g<0> ",
            ),  
        ]

        # Pads parentheses
        self.parantheses = (re.compile(r"[\]\[\(\)\{\}\<\>]"), r" \g<0> ")

        self.double_dashes = (re.compile(r"--"), r" -- ")

    def single_sent_tokenize(self, text: str,  return_str: bool = False):
        """Return a tokenized copy of `text`.
        :param text: A string with a sentence.
        :type text: str
        :param return_str: If True, return tokens as space-separated string,
            defaults to False.
        :type return_str: bool, optional
        :return: List of tokens from `text`.
        :rtype: List[str]
        """
        if return_str:
            warnings.warn(
                "Parameter 'return_str' has been deprecated and should no "
                "longer be used.",
                category=DeprecationWarning,
                stacklevel=2,
            )

        for regexp, substitution in self.start_quotations:
            text = regexp.sub(substitution, text)

        for regexp, substitution in self.punctuation:
            text = regexp.sub(substitution, text)

        # Handles parentheses.
        regexp, substitution = self.parantheses
        text = regexp.sub(substitution, text)
       

        # Handles double dash.
        regexp, substitution = self.double_dashes
        text = regexp.sub(substitution, text)

        # add extra space to make things easier
        text = " " + text + " "

        for regexp, substitution in self.end_quotations:
            text = regexp.sub(substitution, text)

        return text.split()
    
    def sent_tokenize(self,text):
        """
        Return a list of sentences in a text corpus. Built using NLTK pretrained punkt model for english. 
        :param text: A string of a text corpus
        :type text: str
        :return: List of sentences[string] from a text
        :rtype: List[str]
        """
        path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(path, "english.pickle")
        with open(file_path,"rb") as file:
            data = pickle.load(file)
            

        return data.tokenize(text)
    
    def word_tokenize(self, text):
        """
        Return a list of tokens for a text corpus. 
        :param text: A string of a text corpus.
        :type text: str
        :return: List of tokens for a text 
        :rtype: List[str]
        """
        sent_tokens = self.sent_tokenize(text)
        tokens = []

        for sent in sent_tokens:
            tokens.extend(self.single_sent_tokenize(sent))
        return tokens

# Devanagari Tokenizers 

class devanagariTokenizer():
    def __init__(self):
        self.start_quotations = [
            (re.compile("([«“‘„]|[`]+)", re.U), r" \1 "),
            (re.compile(r"^\""), r"``"),
            (re.compile(r"(``)"), r" \1 "),
            (re.compile(r"([ \(\[{<])(\"|\'{2})"), r"\1 `` "),
        ]
        self.end_quotations = [
            (re.compile("([»”’])", re.U), r" \1 "),
            (re.compile(r"''"), " '' "),
            (re.compile(r'"'), " '' "),
        ]

        self.punctuation = [
          

            (re.compile(r"([,])([^\d])"), r" \1 \2"),#This pattern matches any colon or comma that is not followed by a digit
                                                    #and adds spaces before and after it.

            (re.compile(r"([,])$"), r" \1 "),#This pattern matches any colon or comma that is at the end of a sentence, and adds a space before it.

            # considering colon at end of sentence as ardhaviram
            # no colon is not considered as seperate colon, it considered as ardhaviram instead. 

            (re.compile(r"[;@#$%&]"), r" \g<0> "), # This pattern matches any of the specified punctuation characters 
                                                #and adds spaces before and after them.
            

            (re.compile(r"[?!।॥]"), r" \g<0> "), #his pattern matches any exclamation point or question mark or danda or double danda
                                                # and adds spaces before and after it.

            (re.compile(r"([^'])' "), r"\1 ' "), #This pattern matches any single quote that is not preceded by 
                                                #another single quote (which would indicate a contraction) and adds a space before and after it.
            (                                    
                re.compile(r"[*]", re.U), #This pattern matches any asterisk and adds spaces before and after it.
                r" \g<0> ",
            ),  
        ]

        self.parantheses = (re.compile(r"[\]\[\(\)\{\}\<\>]"), r" \g<0> ")
        self.double_dashes = (re.compile(r"--"), r" -- ")

    def single_sent_tokenizer(self, text):

        for regexp, substitution in self.start_quotations:
            text = regexp.sub(substitution, text)

        for regexp, substitution in self.punctuation:
            text = regexp.sub(substitution, text)

        # Handles parentheses.
        regexp, substitution = self.parantheses
        text = regexp.sub(substitution, text)
       

        # Handles double dash.
        regexp, substitution = self.double_dashes
        text = regexp.sub(substitution, text)

        # add extra space to make things easier
        text = " " + text + " "

        for regexp, substitution in self.end_quotations:
            text = regexp.sub(substitution, text)

        return text.split()
    
    def word_tokenize(self, text):
        sent_tokens =  self.sent_tokenize(text)
        tokens = []

        for sent in sent_tokens:
            tokens.extend(self.single_sent_tokenizer(sent))
        return tokens
    def sent_tokenize(self,text):
        pattern = '(?<=[?!।॥])\s'
        text = re.sub(r'[\r\n]+', ' ', text)

        # Tokenize the text into sentences
        sentences = re.split(pattern, text)

        # Remove leading/trailing white space from each sentence
        sentences = [s.strip() for s in sentences]

        return sentences
    
# Roman Devangari Mixed Tokenizers 

class RomanDevanagariTokenizer():
    def __init__(self):

        # Starting quotes 
        self.start_quotations = [
            (re.compile("([«“‘„]|[`]+)", re.U), r" \1 "),
            (re.compile(r"^\""), r"``"),
            (re.compile(r"(``)"), r" \1 "),
            (re.compile(r"([ \(\[{<])(\"|\'{2})"), r"\1 `` "),
            (re.compile(r"(?i)(\')(?!re|ve|ll|m|t|s|d|n)(\w)\b", re.U), r"\1 \2"), # To deal with can't to "can" and "'t". 
        ]
        # Ending quotes.
        self.end_quotations = [
            (re.compile("([»”’])", re.U), r" \1 "),
            (re.compile(r"''"), " '' "),
            (re.compile(r'"'), " '' "),
            (re.compile(r"([^' ])('[sS]|'[mM]|'[dD]|') "), r"\1 \2 "),
            (re.compile(r"([^' ])('ll|'LL|'re|'RE|'ve|'VE|n't|N'T) "), r"\1 \2 "), # to deal with they'll aren't etc. 
        ]

        # Punctuation.
        self.punctuation = [
            (re.compile(r'([^\.])(\.)([\]\)}>"\'' "»”’ " r"]*)\s*$", re.U), r"\1 \2 \3 "), #This pattern matches a period that is not at the end of a sentence
                                                                                            # adds space before and after period.
            # for devanagari we treat colon just after a word as ardhaviram 
            (re.compile(r"(?<![ऀ-ॿ])([:])([^\d])"), r" \1 \2"),#This pattern matches any colon that is not followed by a digit
                                                    #and adds spaces before and after it.

            (re.compile(r"(?<![ऀ-ॿ])([:])$"), r" \1 "),#This pattern matches any colon that is at the end of a sentence, and adds a space before it.

            # For comma not followed by digit 
            (re.compile(r"([,])([^\d])"), r" \1 \2"),
            # for comma at end 
            (re.compile(r"([,])$"), r" \1 "),

            (
                re.compile(r"\.{2,}", re.U), #This pattern matches two or more consecutive periods (i.e., ellipses) 
                r" \g<0> ",                  #and adds spaces before and after them.
            ),  

            (re.compile(r"[;@#$%&]"), r" \g<0> "), # This pattern matches any of the specified punctuation characters 
                                                #and adds spaces before and after them.
            (                                      
                re.compile(r'([^\.])(\.)([\]\)}>"\']*)\s*$'), #This pattern handles the final period in a text, matching any period that is at the end of a sentence and adding a space before it. 
                r"\1 \2\3 ",                                  #It also captures any punctuation that follows the period and adds it back in after the space
            ),  # Handles the final period.

            (re.compile(r"[?!।॥]"), r" \g<0> "), #his pattern matches any exclamation point or question mark and adds spaces before and after it.

            (re.compile(r"([^'])' "), r"\1 ' "), #This pattern matches any single quote that is not preceded by 
                                                #another single quote (which would indicate a contraction) and adds a space before and after it.
            (                                    
                re.compile(r"[*]", re.U), #This pattern matches any asterisk and adds spaces before and after it.
                r" \g<0> ",
            ),  
        ]

        self.parantheses = (re.compile(r"[\]\[\(\)\{\}\<\>]"), r" \g<0> ")

        self.double_dashes = (re.compile(r"--"), r" -- ")

    def single_sent_tokenize(self, text: str,  return_str: bool = False):
        r"""Return a tokenized copy of `text`.
        :param text: A string with a sentence or sentences.
        :type text: str
        :param return_str: If True, return tokens as space-separated string,
            defaults to False.
        :type return_str: bool, optional
        :return: List of tokens from `text`.
        :rtype: List[str]
        """
        if return_str:
            warnings.warn(
                "Parameter 'return_str' has been deprecated and should no "
                "longer be used.",
                category=DeprecationWarning,
                stacklevel=2,
            )

        for regexp, substitution in self.start_quotations:
            text = regexp.sub(substitution, text)

        for regexp, substitution in self.punctuation:
            text = regexp.sub(substitution, text)

        # Handles parentheses.
        regexp, substitution = self.parantheses
        text = regexp.sub(substitution, text)
       

        # Handles double dash.
        regexp, substitution = self.double_dashes
        text = regexp.sub(substitution, text)

        # add extra space to make things easier
        text = " " + text + " "

        for regexp, substitution in self.end_quotations:
            text = regexp.sub(substitution, text)

        return text.split()
    
    def word_tokenize(self, text):
        sent_tokens =  self.sent_tokenize(text)
        tokens = []

        for sent in sent_tokens:
            tokens.extend(self.single_sent_tokenize(sent))
        return tokens
    
    def sent_tokenize(self,text):
        # pattern for devanagari sentence tokenization
        pattern = '(?<=[।॥])\s'
        text = re.sub(r'[\r\n]+', ' ', text)

        path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(path, "english.pickle")
        with open(file_path,"rb") as file:
            data = pickle.load(file)
        eng_sent_tokenized = data.tokenize(text)

    # Tokenize the text into sentences
        final_sentences = []
        for sent in eng_sent_tokenized:
            sentences = re.split(pattern, sent)
            final_sentences.extend(sentences)
    

    # Remove leading/trailing white space from each sentence
        final_sentences = [s.strip() for s in final_sentences]

        return final_sentences
    