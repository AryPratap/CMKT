from fastai.text import *
from googletrans import Translator
import re
from cmkt.preprocessing.stemmer.stemmer import *
from cmkt.tasks import TaskToolKit

# words_dict  = { "तैराक":"तैर",
#                 "चालाक":"चाल",
#                 "कूलाक":"कूल",
#                 "बेलन":"बेल",
#                 "मिलाप":"मिल",
#                 "चुपचाप": "चुप",
#                 "निकास":"निकस",
#                 "लुकास":"लुक",
#                 }

# suffixes = {
# 	    1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],  
#             2: ["तृ","ान","ैत","ने","ाऊ","ाव","कर", "ाओ", "िए", "ाई", "ाए", "नी", "ना", "ते", "ीं", "ती",
#                 "ता", "ाँ", "ां", "ों", "ें","ीय", "ति","या", "पन", "पा","ित","ीन","लु","यत","वट","लू"],     
#             3: ["ेरा","त्व","नीय","ौनी","ौवल","ौती","ौता","ापा","वास","हास","काल","पान","न्त","ौना","सार","पोश","नाक",
#                 "ियल","ैया", "ौटी","ावा","ाहट","िया","हार", "ाकर", "ाइए", "ाईं", "ाया", "ेगी", "वान", "बीन",
#                 "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं","कला","िमा","कार",
#                 "गार", "दान","खोर"],     
#             4: ["ावास","कलाप","हारा","तव्य","वैया", "वाला", "ाएगी", "ाएगा", "ाओगी", "ाओगे", 
#                 "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां",
#                 "त्वा","तव्य","कल्प","िष्ठ","जादा","क्कड़"],     
#             5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां", "अक्कड़","तव्य:","निष्ठ"],
# }

# special_suffixes = ["र्", "ज्य","त्य"]
# dict_special_suffixes = {"र्":"ृ",
#                          "ज्य":"ज्",
#                          "त्य":"त्"}

# def hi_stem(word, clean=False,chars=None):
#     if clean == True:
#         word = clean_text(word, chars)
    
#     ans = word
#     bl = False
    
#     if word in words_dict.keys():
#         return words_dict[word]
    
#     for L in 5, 4, 3, 2, 1:
#         if len(word) > L + 1:
#             for suf in suffixes[L]:
#                 if word.endswith(suf):
#                     ans = word[:-L]
#                     bl =True
#         if bl == True:
#             break
                    
#     if bl == True:
#         for suf in suffixes[1]:
#             if ans.endswith(suf):
#                 # use case - गानेवाला
#                 ans = hi_stem(ans)
   
#     for suf in special_suffixes:
#         if ans.endswith(suf):
#             l = len(suf)
#             ans = ans[:-l]
#             ans += dict_special_suffixes[suf]
 
#     return ans

# def clean_text(text, chars=None):
#     if chars == None:        
#         text = re.sub(r"[()\"#/@;:<>{}`+=~|!?,']", "", text)
#     else:
#         text = re.sub(r"[" +chars+ "()\"#/@;:<>{}`+=~|!?,']", "", text)
#     return text

# def hindi_stem(text):
#     ans = ""
#     for i in text.split(' '):
#         ans += hi_stem(i)
#         ans += " "

#     return ans

# def hien_stemmer(text):
#   results = []
  
#   hientoolkit = TaskToolKit("hineng")
  
#   lid = hientoolkit.lid(model_name="XLM Roberta base")
#   translator = Translator()
#   en_stemmer = PorterStemmer()

#   tokens_tags_list = lid.getLangTags(text)

#   for i in tokens_tags_list:
#     if(i[1] == 'EN'):
#       results.append(en_stemmer.stem(i[0]))
#     elif(i[1] == "HI"):
#       hi_token = translator.translate(i[0], src = 'hi', dest = 'hi').text
#       if (bool(re.match(r"^[A-Za-z]", hi_token))):
#         hi_token = translator.translate(i[0], src = 'hi', dest = 'hi')
#       results.append(hindi_stem(hi_token))

#   return results
LANGUAGES = ['hi','en','hineng']

class Stemmer:
    def __init__(self,lang): 
        self.words_dict  = { "तैराक":"तैर",
                "चालाक":"चाल",
                "कूलाक":"कूल",
                "बेलन":"बेल",
                "मिलाप":"मिल",
                "चुपचाप": "चुप",
                "निकास":"निकस",
                "लुकास":"लुक",
                }
        self.suffixes = {
	        1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],  
            2: ["तृ","ान","ैत","ने","ाऊ","ाव","कर", "ाओ", "िए", "ाई", "ाए", "नी", "ना", "ते", "ीं", "ती",
                "ता", "ाँ", "ां", "ों", "ें","ीय", "ति","या", "पन", "पा","ित","ीन","लु","यत","वट","लू"],     
            3: ["ेरा","त्व","नीय","ौनी","ौवल","ौती","ौता","ापा","वास","हास","काल","पान","न्त","ौना","सार","पोश","नाक",
                "ियल","ैया", "ौटी","ावा","ाहट","िया","हार", "ाकर", "ाइए", "ाईं", "ाया", "ेगी", "वान", "बीन",
                "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं","कला","िमा","कार",
                "गार", "दान","खोर"],     
            4: ["ावास","कलाप","हारा","तव्य","वैया", "वाला", "ाएगी", "ाएगा", "ाओगी", "ाओगे", 
                "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां",
                "त्वा","तव्य","कल्प","िष्ठ","जादा","क्कड़"],     
            5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां", "अक्कड़","तव्य:","निष्ठ"],
        }

        self.special_suffixes = ["र्", "ज्य","त्य"]
        self.dict_special_suffixes = {"र्":"ृ",
                         "ज्य":"ज्",
                         "त्य":"त्"}
        
        self.lang = lang

        if (lang.lower() not in LANGUAGES):
            raise ValueError(f'{self.lang} language not supported')

        
    def hi_stem(self,word, clean=False,chars=None):
        if clean == True:
            word = self.clean_text(word, chars)
        
        ans = word
        bl = False
        
        if word in self.words_dict.keys():
            return self.words_dict[word]
        
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in self.suffixes[L]:
                    if word.endswith(suf):
                        ans = word[:-L]
                        bl =True
            if bl == True:
                break
                        
        if bl == True:
            for suf in self.suffixes[1]:
                if ans.endswith(suf):
                    # use case - गानेवाला
                    ans = self.hi_stem(ans)
    
        for suf in self.special_suffixes:
            if ans.endswith(suf):
                l = len(suf)
                ans = ans[:-l]
                ans += self.dict_special_suffixes[suf]
    
        return ans
    
    def clean_text(self,text, chars=None):
        if chars == None:        
            text = re.sub(r"[()\"#/@;:<>{}`+=~|!?,']", "", text)
        else:
            text = re.sub(r"[" +chars+ "()\"#/@;:<>{}`+=~|!?,']", "", text)
        return text
    
    def stem(self,text):
        
        if self.lang.lower() == 'hi':
            ans = ""
            for i in text.split(' '):
                ans += self.hi_stem(i)
                ans += " "

            return ans
        
        elif self.lang.lower() == 'en':
            eng_stemmer = PorterStemmer()
            stemmed = eng_stemmer.stem(text)
            return stemmed
        
        elif self.lang.lower() == 'hineng':
            results = []
        
            hientoolkit = TaskToolKit("hineng")
            
            lid = hientoolkit.lid(model_name="XLM Roberta base")
            translator = Translator()
            en_stemmer = PorterStemmer()

            tokens_tags_list = lid.getLangTags(text)

            for i in tokens_tags_list:
                if(i[1] == 'EN'):
                    results.append(en_stemmer.stem(i[0]))
                elif(i[1] == "HI"):
                    hi_token = translator.translate(i[0], src = 'hi', dest = 'hi').text
                    if (bool(re.match(r"^[A-Za-z]", hi_token))):
                        hi_token = translator.translate(i[0], src = 'hi', dest = 'hi')
                        
                    hi_token_ans = ""
                    for i in hi_token.split(' '):
                        hi_token_ans += self.hi_stem(i)
                        hi_token_ans += " "
                    results.append(hi_token_ans)

            return results

    # def hindi_stem(self,text):
    #     ans = ""
    #     for i in text.split(' '):
    #         ans += self.hi_stem(i)
    #         ans += " "

    #     return ans
    
    # def eng_stem(self,text):
    #     eng_stemmer = PorterStemmer()
    #     stemmed = eng_stemmer.stem(text)

    #     return stemmed
    
    # def hien_stemmer(self,text):
    #     results = []
        
    #     hientoolkit = TaskToolKit("hineng")
        
    #     lid = hientoolkit.lid(model_name="XLM Roberta base")
    #     translator = Translator()
    #     en_stemmer = PorterStemmer()

    #     tokens_tags_list = lid.getLangTags(text)

    #     for i in tokens_tags_list:
    #         if(i[1] == 'EN'):
    #             results.append(en_stemmer.stem(i[0]))
    #         elif(i[1] == "HI"):
    #             hi_token = translator.translate(i[0], src = 'hi', dest = 'hi').text
    #             if (bool(re.match(r"^[A-Za-z]", hi_token))):
    #                 hi_token = translator.translate(i[0], src = 'hi', dest = 'hi')
    #             results.append(self.hindi_stem(hi_token))

    #     return results


