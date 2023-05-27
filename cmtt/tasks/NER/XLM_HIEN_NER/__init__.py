from transformers import AutoModelForTokenClassification, AutoTokenizer
from cmtt.preprocessing import RomanTokenizer
import torch 
from pathlib import Path
import os 

path = Path(__file__).parent

model_name = "AryPratap/XLM-roberta-HIEN-NER"

class XLM_HIEN_NER():

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
            "0": "O",
            "1": "B-ORGANISATION",
            "2": "I-ORGANISATION",
            "3": "B-PLACE",
            "4": "I-PLACE",
            "5": "B-PERSON",
            "6": "I-PERSON"
        }

    def getNERTags(self,text):

        #tokens1 = ['Aap', 'kaise', 'hai', 'main', 'thik','.','I','am','good','.']
        word_tokens = self.wordTokenizer.word_tokenize(text)
        tokens = self.tokenizer(word_tokens, is_split_into_words = True, return_tensors="pt")
        outputs = self.model(**tokens)
        predicted_labels = outputs.logits.argmax(dim=-1).tolist()
        predicted_labels = predicted_labels[0]
        predicted_labels = predicted_labels[1:-1]

        word_ids = tokens.word_ids()
        word_ids = word_ids[1:-1]
        ner_labels = [predicted_labels[0]]
        for i in range(1,len(word_ids)):
            if word_ids[i] != word_ids[i-1]:
                ner_labels.append(predicted_labels[i])

        ner_tags = [self.id2label[str(label)] for label in ner_labels]

        return_list = []
        for i in range(len(word_tokens)):
            return_list.append((word_tokens[i],ner_tags[i]))

        return return_list
    


#model = XLM_Roberta_HIEN()

#tags = model.getlangIds("Aap kaise hai main thik. I am good.")

#print(tags)



