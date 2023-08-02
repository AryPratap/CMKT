from cmkt.tasks import TaskToolKit
import numpy as np
from cmkt.metrics.scores import *


class CodeMixedMetrics:
	"""
    CodeMixedMetrics provides functionality to calculate various code-mixing metrics for a sentence.

    Available metrics: cmi, M-Index, I-Index, burstiness

    Two-way computation is offered:
    1. If only the sentence is provided: In this method, enter the sentence along with the required metric name, and
       the function will handle the rest.

    2. If custom language tags are provided in the langTags input variable.

    The code-mixed metrics allow calculation for code-mixed sentences with at most 2 languages.
    Custom langTags should be a list of strings like ['1', '1', '0', '0', '0', '1', '3', '4'],
    where:
    '1' represents language-1 tokens
    '0' represents language-2 tokens
    The rest represent language-independent tokens.
    
    Example usage:
    Case-1, With only sentence as input
    
    >>> sent = "RAHUL jab dieting par hota hai toh green tea peeta hai."
	>>> metrics = CodeMixedMetrics(language="hineng")

	>>> # Code-Mixing Index 
	>>> print(metrics.metrics(name="cmi", sentence=sent))
		30.000000000000004

	>>> # M-Index 
	>>> print(metrics.metrics(name="M-Index", sentence=sent))
		0.661290322580645
	
	Case-2, with custom language tags

	>>> print(metrics.metrics(name="cmi, langTags = ['2', '1','0','1','1','1','1','0','0','1','1']))
		30.000000000000004
	
	# In above example, '1' --> hindi token, '0'--> english token, '2'-->language independent token. Similarly any sentence can be represented 
	as language tags for each token of the sentence. 

    """
	def __init__(self, language):
		self.language = language
		self.mytoolkit = TaskToolKit('hineng')
		self.lid = self.mytoolkit.lid(model_name="xlm-roberta-base")
		self.ner = self.mytoolkit.ner(model_name="xlm-roberta-base")


	def AvailableMetrics(self):
		return ["cmi", "M-index", "I-index", "burstiness"]

	def metrics(self,name, sentence, langTags = None):
		"""
		This function is repsonsible to calculate the code-mixing metrics aas mentioned above.
		Args:
			:type name: str
			:param name: name of metrics to be computed, name can any of these, ["cmi", "M-index", "I-index", "burstiness"]
						 the metrics name is case sensitive. 
			:type sentence: str
			:param sentence: code-mixed sentence.

			:type langTags: List[str]
			:param langTags: custom token wise language tags for the input sentence.  
		Returns:
			Returns the specified metrics
			:rtype: float
		"""

		if name not in self.AvailableMetrics():
			raise KeyError(f'{name} metrics not found.')
		
		if langTags is None:

			langTags = self.lid.getlangIds(sentence)
			nertags = self.ner.get_predictions(sentence)	
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
			
		elif name == "M-index":
					
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
		
		elif name == "I-index":
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
		


