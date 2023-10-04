# coding=utf-8

"""UzWordCriteriaMatcher Module"""

import json

from extractor import extractor


with open('data\\uzbek_words.json', 'r', encoding='utf-8') as json_file:
    uzbek_words_data = json.load(json_file)

# Implementing replacements before searching for words
def modify_word(word):
    return word.replace('ʼ', '').replace('-', '')

# FindWordsMatchingCriteria
def FindWordsMatchingCriteria(input_text, max_tokens=None):

    # Extract criteria from input text using the `CriExtractor` function from `extractor.py` module
    criteria = extractor.CriExtractor(input_text)

    # Check if criteria is empty
    if not criteria:
        print("")
        return []
    
    matching_words = []

    modified_words = {word: modify_word(word) for word in uzbek_words_data}

    for word, modified_word in modified_words.items():
        # Check if the word meets all the criteria extracted by the CriExtractor function
        meets_criteria = True

        # Check starting character, if specified
        if 'starting_char' in criteria:
            if modified_word[0] != criteria['starting_char']:
                meets_criteria = False

        # Check ending character, if specified
        if 'ending_char' in criteria:
            if modified_word[-1] != criteria['ending_char']:
                meets_criteria = False

        # Check specific character positions, if specified
        for key in criteria.keys():
            if key.startswith('char_'):
                position = int(key.split('_')[1])
                if len(modified_word) > position - 1 and modified_word[position - 1] != criteria[key]:
                    meets_criteria = False

        # Check the number of characters, if specified
        if 'n_of_char' in criteria:
            if len(modified_word) != int(criteria['n_of_char']):
                meets_criteria = False

        # If the word meets all criteria, add it to the list of matching words
        if meets_criteria:
            matching_words.append(word)

    # max_tokens
    if max_tokens is not None and len(matching_words) > max_tokens:
        matching_words = matching_words[:max_tokens]

    return matching_words
