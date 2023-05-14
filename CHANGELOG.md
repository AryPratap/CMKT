# CHANGELOG
All notable changes to this project will be documented in this file.

## [Unreleased]
- [ ] Add sphinx docs.
- [ ] Mutilingual stemmer using LID.
- [ ] Token and sentence level tasks - Sentence labelling (positive or negative).
- [ ] Fake news or not.
- [ ] Sequence to sequence. Given a sentence you output a sentence.
- [ ] Generation tasks.
- [ ] Make Bi-LSTM model's performance comparable to that of Microsoft LID.
- [ ] Make model functional for text in devanagari script as well.
- [ ] Add lang parameters to tokenizers.
- [ ] 4th module could be metrics. Code mixing Index - advanced and .., accuracy, f score, blue scores, and more.
- [ ] Function to delete the cmtt folder that gets created when downloading anything using cmtt.
- [ ] List of all of models for each task and their details - Accuracy, Trained on what, score and every other detail possible.
- [ ] Option to list all details or just the names of the models for each task. Something like models(task = LID) and models(details=True).
- [ ] Try to complete tasks module.
- [ ] Have a look at NLTK's License. And check whether to cite or not everything or not. Citing.
- [ ] Clean code. Clean up the repo. Remove unnecessary. Don't reinvent when not necessary. 
- [ ] Update the project hierarchy.

## [0.8.0]
- Added submodules POS (Part of Speech Tagging) for Hindi-English code-mixed text.
- Added submodules NER (Named Entity Recognition) for Hindi-English code-mixed text.
- Restructured LID, POS and NER submodules to be part of new module tasks.
- Added new demo files and updated documentation.

## [0.7.5]
- Added submodule LID (Language Identification) for Hindi-English code-mixed text.
- Added stemmer (hien_stemmer) for Hindi-English text (uses LID and transliteration).
- Updated stemmer for English, added support for sentences.
- Updated demo files and documentation.

## [0.7.0]
- Added rule based word and character tokenizers for devanagari text.
- Added stemmer for english words.
- Added detokenizers.
- Added testcases for all data functions.
- Made output consistent across tokenizers.
- Updated the project documentation and demo files.

## [0.6.0]
- Added search parameters in list_cmtt_datasets function.
- Added testcases for all tokenizers.
- Added tokenizers.md file for information regarding the tokenizers implemented.
- Fixed Wordpiece tokenizer.
- Updated Whitespace tokenizer.
- Updated the project documentation and demo files.

## [0.5.0]
- Added changelog file to keep list of notable changes for each version of this project.
- Added sentence piece based tokenizers for hindi and hinglish.
- Added demo folder for testing out cmtt (installed using pip).
- Updated the project documentation.

## [0.3.0]
- Archived previous repo for code_mixed_text_toolkit.
- Fixed download issue for different operating systems. Tested on Kali OS.
- Added preprocessing subpackage to cmtt.
- Added language pairs hierarchy for cmtt dataset downloads.
- Changed Wordpiece tokenizer (erroneous, to be fixed in a later version).
- Changed tests for Wordpiece tokenizer (erroneous, to be fixed in a later version).

## [0.1.0]
- Published new package cmtt, replacing code_mixed_text_toolkit.
- Simplified how cmtt package is imported by users.
- Added data subpackage to cmtt.
- Added new tests for cmtt.
- Updated cmtt datasets information.