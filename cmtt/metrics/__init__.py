from cmtt.tasks import TaskToolKit
import numpy as np



class Metrics:
	def __init__(self, language):
		self.language = language

	def AvailableMetrics(self):
		return ["cmi", "M-Index", "I-Index", "burstiness"]

	def metrics(self,name, sentence):

		if name not in self.AvailableMetrics():
			raise KeyError(f'{name} metrics not found.')
		
		mytoolkit = TaskToolKit(self.language)
		lid = mytoolkit.lid(model_name="XLM Roberta base")

		langTags = lid.getlangIds(sentence)
		ner = mytoolkit.ner(model_name="XLM Roberta base")
		nertags = ner.getNERTags(sentence)	
		for i in range(len(langTags)):
				if nertags[i][1] != 'O':
					langTags[i] = '8'

		if name == "cmi":
			
					
			lang1_words = 0
			for i in langTags:
				if i == '0':
					lang1_words = lang1_words + 1
				
			lang2_words = 0
			for i in langTags:
				if i == '1':
					lang2_words = lang2_words + 1
				
			max_count = max(lang1_words,lang2_words)

			# total tokens 
			n = len(langTags)
			# language independent tokens
			u = len(langTags) - lang1_words - lang2_words

			if n>u:
				return 100*(1 - (max_count/(n-u)))
			return 0
			
		elif name == "M-Index":
					
			lang1_words = 0
			for i in langTags:
				if i == '0':
					lang1_words = lang1_words + 1
				
			lang2_words = 0
			for i in langTags:
				if i == '1':
					lang2_words = lang2_words + 1
		
			# total number of words 
			n = len(langTags)
			# total languages 
			k = 3

			# language independent words
			lang3_words = n - lang1_words - lang2_words
			if lang3_words == 0:
				k = 2
		
			sigma_pj = (lang1_words/n)**2 + (lang2_words/n)**2 + (lang3_words/n)**2 

			return (1- sigma_pj)/((k-1)*sigma_pj)
		
		elif name == "I-Index":
			S = 0

			for i in range(len(langTags)-1):
				if langTags[i]!=langTags[i+1]:
					S = S+1
			return S/(len(langTags)-1)
		
		elif name == "burstiness":
			# Calculate the language spans
			spans = []
			current_span = 1
			for i in range(1, len(langTags)):
				if langTags[i] == langTags[i-1]:
					current_span += 1
				else:
					spans.append(current_span)
					current_span = 1
			spans.append(current_span)

			# Calculate the mean and standard deviation of language spans
			mr = np.mean(spans)
			sigma_r = np.std(spans)

			# Calculate burstiness
			burstiness = (sigma_r - mr) / (sigma_r + mr)
			return burstiness
		
def accuracy(reference, test):
    

    if len(reference) != len(test):
        raise ValueError("Lists must have the same length.")
    return sum(x == y for x, y in zip(reference, test)) / len(test)

def precision(reference, test):
    

    if not hasattr(reference, "intersection") or not hasattr(test, "intersection"):
        raise TypeError("reference and test should be sets")

    if len(test) == 0:
        return None
    else:
        return len(reference.intersection(test)) / len(test)
		
def recall(reference, test):
    
    if not hasattr(reference, "intersection") or not hasattr(test, "intersection"):
        raise TypeError("reference and test should be sets")

    if len(reference) == 0:
        return None
    else:
        return len(reference.intersection(test)) / len(reference)
    

def f_measure(reference, test, alpha=0.5):
    
    p = precision(reference, test)
    r = recall(reference, test)
    if p is None or r is None:
        return None
    if p == 0 or r == 0:
        return 0
    return 1.0 / (alpha / p + (1 - alpha) / r)

def cosine_similarity(x, y):
    
    # Ensure length of x and y are the same
    if len(x) != len(y) :
        return None
    
    # Compute the dot product between x and y
    dot_product = np.dot(x, y)
    
    # Compute the L2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum(x**2)) 
    magnitude_y = np.sqrt(np.sum(y**2))
    
    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    
    return cosine_similarity

