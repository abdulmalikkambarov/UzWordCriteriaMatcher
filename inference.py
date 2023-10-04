# coding=utf-8

"""Inference"""

from module import FindWordsMatchingCriteria
from extractor.extractor import CriExtractor


def OpeningSen(criteria):
    criteria_sentences = []
    if 'starting_char' in criteria:
        criteria_sentences.append(f"“{criteria['starting_char'].upper()}” harfi bilan boshlanadigan")
    if 'ending_char' in criteria:
        criteria_sentences.append(f"“{criteria['ending_char'].upper()}” harfi bilan tugaydigan")
    for key in criteria.keys():
        if key.startswith('char_'):
            position = int(key.split('_')[1])
            criteria_sentences.append(f"{position}-harfi “{criteria[key].upper()}” bõlgan")
    if 'n_of_char' in criteria:
        criteria_sentences.append(f"jami {criteria['n_of_char']} ta harfdan tashkil topgan")

    if len(criteria_sentences) > 1:
        last_sentence = criteria_sentences.pop()
        return ', '.join(criteria_sentences) + ' va ' + last_sentence
    else:
        return ', '.join(criteria_sentences)

if __name__ == '__main__':
    input_text = "o harfi bilan boshlanib, a tortinchi harfi boʻlgan va jami 4 ta harfdan tashkil topgan soʻzlarni top"
    matching_words = FindWordsMatchingCriteria(input_text, max_tokens=10)
    criteria = CriExtractor(input_text)
    formatted_criteria = OpeningSen(criteria)

    if matching_words:
        print(f"Quyida {formatted_criteria} sõzlar rõyxati keltirilgan:")
#       for word in matching_words:
#           print(word)
        for i, word in enumerate(matching_words, start=1):
            print(f"{i}. {word}")

    else:
        print(f"Siz yozgan kriteriylarga mos keladigan sõzlarni ({formatted_criteria}) topa olmadim. Agar sizga boshqa kriteriylarga mos keluvchi sõzlarni topishda yordam kerak bõlsa, tortinmasdan shu yerga yozing!")
