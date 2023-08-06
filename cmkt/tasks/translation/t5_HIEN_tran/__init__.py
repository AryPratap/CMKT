from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import torch 
from pathlib import Path
import os 

path = Path(__file__).parent

model_name = "AryPratap/t5-hinglish-to-en"

class t5_HIEN_tran():

    def __init__(self):

        dest = path/'models/'
        if not (dest).exists(): 
            os.makedirs(dest, exist_ok=True)
            print("Downloading model files..")
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            tokenizer.save_pretrained(dest)
            model.save_pretrained(dest)

        self.model = AutoModelForSeq2SeqLM.from_pretrained(dest)
        self.tokenizer = AutoTokenizer.from_pretrained(dest)
        self.translator = pipeline("translation", model=self.model,tokenizer = self.tokenizer)
        

    def get_predictions(self,text):

        output = self.translator(text)
        prediction = output[0]['translation_text']
        return prediction
    






