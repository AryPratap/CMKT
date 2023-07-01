from cmkt.metrics.scores import *



# Blue Score
predictions = [["hello", "there", "general", "kenobi"], ["foo", "bar", "foobar"]]
references = [[["hello", "there", "general", "kenobi"]],[["foo", "bar", "foobar"]]]

predictions_1 = [["I","have","thirty","six","years"]]
references_1 = [[["I","am","thirty","six","year","old"], ["I","am","thirty","six"]]]

blue = blue_score(predictions=predictions_1, references=references_1)
print(blue)

# Rouge Score

predictions = ["I really loved reading hunder games"]
references = ["I loved reading the hunger games"]
rouge = rouge_score(predictions=predictions, references=references)
print(rouge)
