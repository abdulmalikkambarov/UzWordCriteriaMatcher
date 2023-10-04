# coding=utf-8

"""CriExtractor Module"""

import re

from fuzzywuzzy import fuzz


def CriExtractor(input_text):
    # Implement replacements in the input text
    input_text = re.sub('o[`ʻ’‘ʼ\']', 'õ', input_text)
    input_text = re.sub('g[`ʻ’‘ʼ\']', 'ğ', input_text)
    input_text = re.sub('ikkinchi harfi', '2-harfi', input_text)
    input_text = re.sub('uchinchi harfi', '3-harfi', input_text)
    input_text = re.sub('tõrtinchi harfi', '4-harfi', input_text)
    input_text = re.sub('tortinchi harfi', '4-harfi', input_text)
    input_text = re.sub('beshinchi harfi', '5-harfi', input_text)
    input_text = re.sub('oltinchi harfi', '6-harfi', input_text)
    input_text = re.sub('yettinchi harfi', '7-harfi', input_text)
    input_text = re.sub('sakkizinchi harfi', '8-harfi', input_text)
    input_text = re.sub('tõqqizinchi harfi', '9-harfi', input_text)
    input_text = re.sub('toqqizinchi harfi', '9-harfi', input_text)
    input_text = re.sub('õninchi harfi', '10-harfi', input_text)
    input_text = re.sub('oninchi harfi', '10-harfi', input_text)

    # Phrases to remove
    phrases_to_remove = ['harfi bilan', 'belgisi bilan', 'harf bilan', 'belgi bilan', 'bilan', 'ta', 'harfdan', 'belgidan', 'ʻ', '’', '‘', 'ʼ', '`', '\'']

    # Remove the phrases from the input text
    for phrase in phrases_to_remove:
        input_text = input_text.replace(phrase, '')

    # Tokenize the remaining text into words
    words = re.findall(r'\b\w+\b', input_text.lower())

    criteria = {}

    # Define keywords
    keywords = ['boshlanadigan', 'boshlangan', 'boshlanuvchi', 'boshlanmish', 'birinchi', 'tugaydigan', 'tugagan', 'tugovchi', 'tuganmish', 'oxirgi', 'tashkil', 'iborat', 'shkil', 'ilk', 'sõnggi', 'songgi', 'boshlanib', 'tugab', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']

    # Extract criteria
    for i, word in enumerate(words):
        match = max(keywords, key=lambda keyword: fuzz.ratio(keyword, word))

        if fuzz.ratio(match, word) > 80:
            if match in ['boshlanadigan', 'boshlangan', 'boshlanuvchi', 'boshlanmish', 'boshlanib', 'birinchi', 'ilk']:
                for j, char in enumerate(words[i-1]):
                    if j == 0:
                        criteria['starting_char'] = char
                    else:
                        criteria[f'char_{j+1}'] = char
            elif match in ['tugaydigan', 'tugagan', 'tugovchi', 'tuganmish', 'tugab', 'oxirgi', 'sõnggi', 'songgi']:
                criteria['ending_char'] = words[i-1]
            elif i < len(words) - 1 and re.match(r'\d+ harfi', words[i] + ' ' + words[i+1]):
                position = re.match(r'(\d+) harfi', words[i] + ' ' + words[i+1]).group(1)
                criteria[f'char_{position}'] = words[i-1]
            elif match in ['tashkil' , 'iborat', 'shkil']:
                criteria['n_of_char'] = words[i-1]

    return criteria

# Test the CriExtractor
# input_text = "m harfi bilan boshlanadigan, s harfi bilan tugaydigan, s 4-harfi boʻlgan va jami 7 ta harfdan tashkil topgan soʻzlarni top."
# print(CriExtractor(input_text))
