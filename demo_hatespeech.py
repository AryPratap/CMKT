from cmkt.tasks import *

mytoolkit = TaskToolKit("hineng")

sentiment_model = mytoolkit.hatespeech("xlm-roberta-base")

text = "Aap bahut ache insaan hain."

prediction = sentiment_model.get_predictions(text)
print(prediction)