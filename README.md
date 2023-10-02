[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



-----------------------------------------
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)![Compatibility](https://img.shields.io/badge/compatible%20with-python3.9.x-blue.svg)
## CMKT: Code-Mixed toolKiT
CMKT is a wrapper library that makes code-mixed text processing more efficient than ever. 
 
## Installation
```
git clone https://github.com/lingo-iitgn/CMKT.git
cd CMKT
pip install -r "requirements.txt"
```
## Getting Started
[Documentation](https://cmkt.readthedocs.io/en/latest/). This page will be updated with more details soon.

How to use this library: <br>
Refer the demo files for toolkit usage or the detailed [Google Colab Notebook](https://colab.research.google.com/drive/11O3ApBUHgWhBe-Pv20KZaw-3o-1lm30h#scrollTo=j-MmU6Et9kZo)
## Modules:
There are four different modules available:-
<br>
- Data Acquisition Module
- Preprocessing Module
- Tasks Module
- Metrics Module
<br>

### Data Acquisition Module
This module enables effortless loading and downloading of datasets in various formats from external and local resources. Additionally, it offers a curated collection of 15 datasets tailored for different NLP tasks specific to Hindi-English code-mixed text. Supported file formats of datasets:- pickle json txt csv conll

Datasets available in cmkt datahub for following tasks. Use the specifed names of tasks to search for datasets in cmkt datahub
```
["lid", "ner", "pos", "machine translation", "sentiment analysis", "hate speech detection", "irony detection", "humor detection", "sarcasm detection"]
```

### Preprocessing Module
Text Preprocessing Module offers a range of functionalities for efficiently preprocessing code-mixed text. This module provides different types of tokenization and stemming specifically designed for code-mixed text. By utilizing the cmkt Text Preprocessing Module, you can efficiently preprocess your code-mixed text data for various downstream tasks such as NLP analysis and model training. 

#### Tokenization
Tokenization in cmkt: Breaking Text into Meaningful Units. <br>
The text preprocessing module includes tokenization techniques at the sentence, word, and subword levels, along with stemming methods for English, Hindi, and Hindi-English mixed script text. Following tokenizers are available in cmkt:-
<br>
- Word Tokenizer
- Sentence Tokenizer
- SentencePiece Tokenizer
<br>
The tokenizers are currently available for english, hindi and english-hindi mixed script text.

#### Stemming 
Stemming in CMKT: Reducing Words to their Base Form <br>
Stemming is an essential part of code-mixed text processing, enabling the reduction of words to their base or root form. In the CMKT , we provide a range of stemmers specifically designed for different languages and language combinations.
<br> 
Following tokenizers are available in cmtt:-
<br>
- English Stemmer
- Hindi Stemmer
- Hindi-English mixed Stemmer

### Tasks Module 
This module provides elementary NLP tasks such as NER, POS, LID etc for code-mixed text. This module also provides functions to search for tasks and models available in cmkt. The Hierarchy of task module is defined below. <br>
Task types available in cmkt: "syntactic", "semantic", and "generational" <br>
TaskToolkit (Language specific)
<br>
syntactic tasks
<br>
- lid
- ner
- pos
<br>
semantic tasks

- sentiment analysis
- hate speech detection
- humor detection
<br>
generational tasks

- machine translation

### Metrics Module 
The metrics module provides a comprehensive range of evaluation metrics, serving diverse needs such as quantifying code-mixed text and assessing the performance of NLP tasks such as classification and machine translation.<br?
Available code-mixed metrics:<br>
- cmi (code-mixed index)
- m-index (Multilingual Index)
- i-index (I-index)
- burstiness
<br> 
Other common metrics available: accuracy, precision, recall, f-meaure, BLUE score, ROUGE score, BERT score, pearson score, spearman score

