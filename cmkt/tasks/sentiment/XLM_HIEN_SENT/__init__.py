from transformers import AutoModelForSequenceClassification, AutoTokenizer

import torch 
from pathlib import Path
import os 

path = Path(__file__).parent

model_name = "AryPratap/XLM-roberta-HIEN-Sentiment-Analysis"

class XLM_HIEN_SENT():

    def __init__(self):

        dest = path/'models/'
        if not (dest).exists(): 
            os.makedirs(dest, exist_ok=True)
            print("Downloading model files..")
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            tokenizer.save_pretrained(dest)
            model.save_pretrained(dest)

        self.model = AutoModelForSequenceClassification.from_pretrained(dest)
        self.tokenizer = AutoTokenizer.from_pretrained(dest)
        self.id2label = {
            0: "neutral",
            1: "negative",
            2: "positive"
        }
        self.label2id = {
            "neutral": 0,
            "negative": 1,
            "positive": 2
        }

    def get_predictions(self,text):

        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits
        
        predicted_class_id = logits.argmax().item()
        prediction = self.model.config.id2label[predicted_class_id]
        return prediction
    





