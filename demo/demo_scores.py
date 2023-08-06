from cmkt.metrics.scores import *
# from sklearn.feature_extraction.text import CountVectorizer
# Accuracy 
reference = 'DET NN VB DET JJ NN NN IN DET NN'.split()
test    = 'DET VB VB DET NN NN NN IN DET NN'.split()
print("Accuracy: ", accuracy(reference, test))
print()

#Precision
reference_set = set(reference)
test_set = set(test)
precision(reference_set, test_set)
print("Precision: ", precision(reference_set, test_set))

# Recall
print("Recall: ", recall(reference_set, test_set))
print()

#F-measure 
print("F-measure: ", f_measure(reference_set, test_set))
print()

# Cosine similarity 
# corpus = [ 'data science is one of the most important fields of science',
#         'this is one of the best data science courses',
#         'data scientists analyze data']

# # Create a matrix to represent the corpus
# X = CountVectorizer().fit_transform(corpus).toarray()

# cos_sim_1_2 = cosine_similarity(X[0, :], X[1, :])
# cos_sim_1_3 = cosine_similarity(X[0, :], X[2, :])
# cos_sim_2_3 = cosine_similarity(X[1, :], X[2, :])

# print('Cosine Similarity between: ')
# print('\tDocument 1 and Document 2: ', cos_sim_1_2)
# print('\tDocument 1 and Document 3: ', cos_sim_1_3)
# print('\tDocument 2 and Document 3: ', cos_sim_2_3)


# Blue Score

predictions = [["I","have","thirty","six","years"]]
references = [[["I","am","thirty","six","year","old"], ["I","am","thirty","six"]]]

blue = blue_score(predictions=predictions, references=references)
print("Blue Score: ", blue)
print()

# Rouge Score

predictions = ["I really loved reading hunder games"]
references = ["I loved reading the hunger games"]
rouge = rouge_score(predictions=predictions, references=references)
print("Rouge Score: ",rouge)
print()

#Spearman Score
spearmanr_metric = spearman_score(references=[1, 2, 3, 4, 5], predictions=[10, 9, 2.5, 6, 4])
print("Spearman Score: ", spearmanr_metric)
print()

#pearson score 

results = pearson_score(predictions=[10, 9, 2.5, 6, 4], references=[1, 2, 3, 4, 5], return_pvalue=True)
print(sorted(list(results.keys())))
print(round(results['pearsonr'], 2))
print(round(results['p-value'], 2))


# bert score 
predictions = ["hello world", "general kenobi"]
references = ["goodnight moon", "the sun is shining"]
results = bert_score(predictions=predictions, references=references, model_type="distilbert-base-uncased")
print(results)
