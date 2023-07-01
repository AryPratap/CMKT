import unicodedata
import os
import re
from urllib.request import urlopen
import pickle
import warnings

SUPPORTED_LANGUAGES = ['hi','en','hineng']

class Tokenizers:
  def __init__(self, lang):
        
        if lang.lower() not in SUPPORTED_LANGUAGES:
           raise ValueError("No tokenizer available for the entered language.")
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

        if lang.lower() == "hi":
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
        else:
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

        self.lang = lang

        

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
        
        # Start quotation
        for regexp, substitution in self.start_quotations:
            text = regexp.sub(substitution, text)
        
       # Punctuation
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

        # end quotation 
        for regexp, substitution in self.end_quotations:
            text = regexp.sub(substitution, text)

        return text.split()
  
  def sent_tokenize(self,text):
        # pattern for devanagari sentence tokenization
        pattern = '(?<=[।॥?!])\s'
        text = re.sub(r'[\r\n]+', ' ', text)

        if self.lang == "hi":
           # Tokenize the text into sentences
          sentences_hi = re.split(pattern, text)

        # Remove leading/trailing white space from each sentence
          sentences_hi = [s.strip() for s in sentences_hi if s.strip()]
          return sentences_hi
        
        else:
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
  
  def word_tokenize(self, text):
        sent_tokens =  self.sent_tokenize(text)
        tokens = []

        for sent in sent_tokens:
            tokens.extend(self.single_sent_tokenize(sent))
        return tokens
  


  





    

      

      
    