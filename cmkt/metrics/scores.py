import numpy as np
from cmkt.metrics.blue_score import compute_bleu
from rouge_score import rouge_scorer, scoring
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from datasets import load_metric

def accuracy(reference, test):
    """
    Calculate the similarity fraction between a list of reference values and a corresponding list of test values. 
    The function returns the ratio of corresponding values that are equal.
    Args:
        :type reference: list
        :param reference: Ordered list of reference values
        :type test: list
        :param test: List of values to be compared with the reference list. 
    Returns:
        Returns the accuracy score for reference and test
        :rtype: float
    """

    if len(reference) != len(test):
        raise ValueError("Lists must have the same length.")
    return sum(x == y for x, y in zip(reference, test)) / len(test)

def precision(reference, test):
    """
    Calculate the inclusion fraction by comparing a set of reference values with a set of test values. 
    The function returns the ratio of test values that appear in the reference set. 
    If the test set is empty, the function returns None.
    Args:
        :type reference: set
        :param reference: A set of reference values.
        :type test: set
        :param test: A set of values to compare against the reference set.
    Returns:
        Returns the precision score for reference and test
        :rtype: float or None

    """
    

    if not hasattr(reference, "intersection") or not hasattr(test, "intersection"):
        raise TypeError("reference and test should be sets")

    if len(test) == 0:
        return None
    else:
        return len(reference.intersection(test)) / len(test)
		
def recall(reference, test):
    """
    Given a set of reference values and a set of test values, return
    the fraction of reference values that appear in the test set.
    If ``reference`` is empty, then return None.
    Args:
        :type reference: set
        :param reference: A set of reference values.
        :type test: set
        :param test: A set of values to compare against the reference set.
    Returns:
        Returns the recall score for reference and test
        :rtype: float or None
    """
    
    if not hasattr(reference, "intersection") or not hasattr(test, "intersection"):
        raise TypeError("reference and test should be sets")

    if len(reference) == 0:
        return None
    else:
        return len(reference.intersection(test)) / len(reference)
    

def f_measure(reference, test, alpha=0.5):
    """
    Given a set of reference values and a set of test values, return
    the f-measure of the test values, when compared against the
    reference values. It is the harmonic mean of precision and recall 
    weighted by alpha. 
    If either ``reference`` or ``test`` is empty, then ``f_measure``
    returns None.
    Args:
        :type reference: set
        :param reference: A set of reference values.
        :type test: set
        :param test: A set of values to compare against the reference set.
    Returns:
        Returns the f1 score for reference and test
        :rtype: float or None

    """
    
    p = precision(reference, test)
    r = recall(reference, test)
    if p is None or r is None:
        return None
    if p == 0 or r == 0:
        return 0
    return 1.0 / (alpha / p + (1 - alpha) / r)

def cosine_similarity(x, y):
    """
    Calculate the cosine similarity between two vectors, x and y.

    The cosine similarity is a measure of similarity between two vectors
    that takes into account the angle between them. It is calculated as
    the dot product of the two vectors divided by the product of their
    magnitudes.

    Args:
        :type x: ndarray
        :param x: First vector
        :type y: ndarray
        :param y: Second vector
    Returns:
        Returns the cosine similarity score between x and y vectors.
        :rtype: float or None
    """
    
    if len(x) != len(y) :
        return None
    
    dot_product = np.dot(x, y)

    magnitude_x = np.sqrt(np.sum(x**2)) 
    magnitude_y = np.sqrt(np.sum(y**2))
    
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    
    return cosine_similarity

def blue_score(predictions, references, max_order=4, smooth=False):
        """
        BLEU (bilingual evaluation understudy) is an algorithm for evaluating the quality of text 
        which has been machine-translated from one natural language to another.
        Refer blue_score.py for more information. 
        Args:
            :type predictions: list
            :param predictions: list of translations to score.
                                Each translation should be tokenized into a list of tokens.

            :type references: list
            :param references: list of lists of references for each translation.
                               Each reference should be tokenized into a list of tokens.

            max_order: Maximum n-gram order to use when computing BLEU score.
            smooth: Whether or not to apply Lin et al. 2004 smoothing.
        Returns:
            'bleu': bleu score,
            'precisions': geometric mean of n-gram precisions,
            'brevity_penalty': brevity penalty,
            'length_ratio': ratio of lengths,
            'translation_length': translation_length,
            'reference_length': reference_length
        """
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

def rouge_score(predictions, references, rouge_types=None, use_aggregator=False, use_stemmer=False):
    """
    CMKT uses the implementation of rouge score from Google Research reimplementation of ROUGE, and the huggingface datasets library.
    For more information visit:
    https://github.com/huggingface/datasets/blob/main/metrics/rouge/rouge.py

    Args:
        predictions: A list of predictions to be scored. Each prediction
        should be a string with tokens separated by spaces.
        references: A list of references for each prediction. Each
        reference should be a string with tokens separated by spaces.
        rouge_types: A list of Rouge types to calculate. Valid names include:
        - "rouge{n}" (e.g., "rouge1", "rouge2") for n-gram based scoring.
        - "rougeL" for Longest Common Subsequence (LCS) based scoring.
        - "rougeLSum" for LCS-based scoring with text splitting using "\n".
        use_stemmer: A boolean indicating whether to use Porter stemmer for word suffix stripping.
        use_aggregator: A boolean indicating whether to return aggregates if set to True.

    Returns:
        rouge1: Rouge-1 scores (precision, recall, f1).
        rouge2: Rouge-2 scores (precision, recall, f1).
        rougeL: Rouge-L scores (precision, recall, f1).
        rougeLsum: Rouge-Lsum scores (precision, recall, f1).


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
    """
    The Spearman rank-order correlation coefficient quantifies the association between two sets of data based on their ranks.
    Args:
        :type predictions: List
        :param predictions: Labels predicted by the model.
        :type references: List
        :param references: Ground Truth Labels.
        :type return_pvalue: bool
        :param return_pvalue: If set True, the p_value will also be returned along with spearman score. 
    Returns:
        Returns the spearman score along with p_value(if set return_pvalue set True).
        :rtype: float
    """
    results = spearmanr(references, predictions)
    if return_pvalue:
        return {"spearmanr": results[0], "spearmanr_pvalue": results[1]}
    else:
        return {"spearmanr": results[0]}


def pearson_score(predictions, references, return_pvalue=False):
        """
        The Spearman rank-order correlation coefficient quantifies the association between two sets of data based on their ranks.
        Args:
            :type predictions: List
            :param predictions: Labels predicted by the model.
            :type references: List
            :param references: Ground Truth Labels.
            :type return_pvalue: bool
            :param return_pvalue: If set True, the p_value will also be returned along with spearman score. 
        Returns:
            Returns the pearson score along with p_value(if set return_pvalue set True).
            :rtype: float
        """
        if return_pvalue:
            results = pearsonr(references, predictions)
            return {"pearsonr": results[0], "p-value": results[1]}
        else:
            return {"pearsonr": float(pearsonr(references, predictions)[0])}
    
def bert_score(predictions,
    references,
    lang=None,
    model_type=None,
    num_layers=None,
    verbose=False,
    idf=False,
    device=None,
    batch_size=64,
    nthreads=4,
    all_layers=False,
    rescale_with_baseline=False,
    baseline_path=None,
    use_fast_tokenizer=False):
    """
    BERTScore uses pre-trained contextual embeddings from BERT to match words in candidate and reference sentences using cosine similarity.
    It correlates well with human judgment for sentence-level and system-level evaluation and provides precision, 
    recall, and F1 measures for assessing language generation tasks.
    CMKT uses the huggingface's datasets library based implementation for bert score 
    for information refer 
    https://github.com/Tiiiger/bert_score#readme 
    https://github.com/huggingface/datasets/tree/main/metrics/bertscore
    """

    bertscore = load_metric("bertscore")
    results = bertscore.compute(predictions=predictions, 
                                references=references, lang=lang,
                                model_type=model_type,
                                num_layers=num_layers,
                                verbose=verbose,
                                idf=idf,
                                device=device,
                                batch_size=batch_size,
                                nthreads=nthreads,
                                all_layers= all_layers,
                                rescale_with_baseline=rescale_with_baseline,
                                baseline_path=baseline_path,
                                use_fast_tokenizer= use_fast_tokenizer)

    return results
    


    

