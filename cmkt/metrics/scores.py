import numpy as np
from cmkt.metrics.blue_score import compute_bleu
from rouge_score import rouge_scorer, scoring
from scipy.stats import spearmanr

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
    
    if len(x) != len(y) :
        return None
    
    dot_product = np.dot(x, y)

    magnitude_x = np.sqrt(np.sum(x**2)) 
    magnitude_y = np.sqrt(np.sum(y**2))
    
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    
    return cosine_similarity

def blue_score(predictions, references, max_order=4, smooth=False):
        score = compute_bleu(
            reference_corpus=references, translation_corpus=predictions, max_order=max_order, smooth=smooth
        )
        (bleu, precisions, bp, ratio, translation_length, reference_length) = score
        return {
            "bleu": bleu,
            "precisions": precisions,
            "brevity_penalty": bp,
            "length_ratio": ratio,
            "translation_length": translation_length,
            "reference_length": reference_length,
        }

def rouge_score(predictions, references, rouge_types=None, use_aggregator=True, use_stemmer=False):
    """
    CMKT uses the implementation of rouge score from Google Research reimplementation of ROUGE, and the huggingface datasets library.
    """
    if rouge_types is None:
            rouge_types = ["rouge1", "rouge2", "rougeL", "rougeLsum"]

    scorer = rouge_scorer.RougeScorer(rouge_types=rouge_types, use_stemmer=use_stemmer)
    if use_aggregator:
        aggregator = scoring.BootstrapAggregator()
    else:
        scores = []

    for ref, pred in zip(references, predictions):
        score = scorer.score(ref, pred)
        if use_aggregator:
            aggregator.add_scores(score)
        else:
            scores.append(score)

    if use_aggregator:
        result = aggregator.aggregate()
    else:
        result = {}
        for key in scores[0]:
            result[key] = [score[key] for score in scores]

    return result

def spearman_score(predictions, references, return_pvalue=False):
    results = spearmanr(references, predictions)
    if return_pvalue:
        return {"spearmanr": results[0], "spearmanr_pvalue": results[1]}
    else:
        return {"spearmanr": results[0]}
    

