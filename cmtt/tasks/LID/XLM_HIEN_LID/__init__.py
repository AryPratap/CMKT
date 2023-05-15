from transformers import AutoModelForTokenClassification, AutoTokenizer
from cmtt.preprocessing import RomanTokenizer
import torch 
from pathlib import Path
import os 

path = Path(__file__).parent

model_name = "AryPratap/XLM-roberta-HIEN-LID"

class XLM_HIEN_LID():
    @classmethod

    def __init__(self):

        dest = path/'models/'
        if not (dest).exists(): 
            os.makedirs(dest, exist_ok=True)
            print("Downloading model files..")
            model = AutoModelForTokenClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            tokenizer.save_pretrained(dest)
            model.save_pretrained(dest)

        self.model = AutoModelForTokenClassification.from_pretrained(dest)
        self.tokenizer = AutoTokenizer.from_pretrained(dest)
        self.wordTokenizer = RomanTokenizer()
        self.id2label = {
            "0": "EN",
            "1": "HI",
            "2": "ne",
            "3": "other",
            "4": "mixed",
            "5": "amniguous",
            "6": "fw",
            "7": "unk"
        }

        self.label2id = {
            "EN" : "0",
            "HI" : "1",
            "ne" : "2",
            "other" : "3",
            "mixed" : "4",
            "amniguous" : "5",
            "fw" : "6",
            "unk" : "7"
        }

    def getLangTags(self,text):

        #tokens1 = ['Aap', 'kaise', 'hai', 'main', 'thik','.','I','am','good','.']
        word_tokens = self.wordTokenizer.word_tokenize(text)
        tokens = self.tokenizer(word_tokens, is_split_into_words = True, return_tensors="pt")
        outputs = self.model(**tokens)
        predicted_labels = outputs.logits.argmax(dim=-1).tolist()
        predicted_labels = predicted_labels[0]
        predicted_labels = predicted_labels[1:-1]

        word_ids = tokens.word_ids()
        word_ids = word_ids[1:-1]
        lang_labels = [predicted_labels[0]]
        for i in range(1,len(word_ids)):
            if word_ids[i] != word_ids[i-1]:
                lang_labels.append(predicted_labels[i])

        lang_tags = [self.id2label[str(label)] for label in lang_labels]

        return_list = []
        for i in range(len(word_tokens)):
            return_list.append((word_tokens[i],lang_tags[i]))

        return return_list
    
    def getlangIds(self,text):

        langtags = self.getLangTags(text)
        langtag_list = []

        for i in langtags:
            langtag_list.append(i[1])

        langIds_list = [self.label2id[str(label)] for label in langtag_list]
        
        return langIds_list


#model = XLM_Roberta_HIEN()

#tags = model.getlangIds("Aap kaise hai main thik. I am good.")

#print(tags)



