#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from S01_TP01_template import get_hamming_distance
from time import perf_counter


def get_words_from_dictionary(file_path, length=None):
    """ Retourne la liste des mots du fichier de nom 'file_name' si 'length' vaut 'None'.
        Sinon retourne la liste des mots de longueur 'length'."""

    result = []

    with open(file_path, 'r', encoding='utf-8') as f:
        words_list = f.readlines()

        for word in words_list:
            word = word[: - 1]
            if (len(word) == length):
                result += [word]
            elif (not length):
                result += [word]

    return result


def get_words_hamming(word, words, hamming_distance):
    """ Retourne une sous-liste de la liste de mots 'words' qui sont à une distance de Hamming
        'hamming_distance' du mot 'word'."""

    list = []

    for word2 in words:
        if (get_hamming_distance(word, word2) == hamming_distance):
            list += [word2]

    return list


def is_perfect_scale(scale):
    """Retourne 'True' si l'échelle de mots 'scale' est parfaite. 'False' sinon. Une échelle de mots est dite parfaite
    si le nombre d'étape pour passer du mot de départ au mot cible est égal à leur distance de hamming."""

    # for mot in scale:
    start_target_words_distance = len(scale) - 1
    first_word = scale[0]
    last_word = scale[start_target_words_distance]

    return get_hamming_distance(first_word, last_word) == start_target_words_distance


def get_removed_words(words_to_remove, all_words):
    """ Retourne une sous-liste des mots de 'all_words' en retirant ceux de 'words_to_remove'"""

    result = [] + all_words

    for word in all_words:
        if (word in words_to_remove):
            result.remove(word)

    return result


def get_next_scales(scale, words):
    """ retourne la liste des échelles de mots possibles constituées par l'échelle de mot 'scale' et un mot de
    la liste 'words'"""

    list = []
    result = []

    for word in words:
        hamming_distance = get_hamming_distance(scale[len(scale) - 1], word)
        if (hamming_distance == 1 and word not in scale):
            list += [word]

    for word in list:
        result += [scale + [word]]

    return result


def get_scale(file_path, word1, word2):
    """ Retourne une échelle de mots entre 'word1' et 'word2' avec les mots du dictionnaire 'file_path'"""

    result = [word1]
    with open(file_path, 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word[:-1]
            hamming_distance = get_hamming_distance(word1, word)
            if (hamming_distance == 1):
                result.append(word)
                if (word == word2):
                    break

    return result


if __name__ == "__main__":
    DICT_NAME = PATH_DICTIONARIES + 'fr_long_dict_cleaned.txt'
    WORD6 = get_words_from_dictionary(DICT_NAME, 6)
    assert WORD6[:9] == ['A-T-IL', 'ABAQUE', 'ABATEE', 'ABATTE',
                         'ABATTU', 'ABBAYE', 'ABCEDE', 'ABERRE', 'ABETIE']
    assert get_words_hamming("ORANGE", WORD6, 0) == ['ORANGE']
    assert get_words_hamming("ORANGE", WORD6, 1) == ['FRANGE', 'GRANGE', 'ORANGS', 'ORANTE',
                                                     'ORONGE']
    assert get_words_hamming("ORANGE", WORD6, 2) == ['BRANDE', 'BRANLE', 'BRANTE', 'CHANGE',
                                                     'CRANTE', 'GRANDE', 'GRINGE', 'ORACLE', 'ORANTS', 'TRANSE',
                                                     'URANIE']
    assert is_perfect_scale(['SUD', 'SUT', 'EUT', 'EST'])
    assert is_perfect_scale(['HOMME', 'COMME', 'COMTE', 'CONTE'])
    assert not is_perfect_scale(['HOMME', 'COMME', 'COMTE', 'CONTE', 'CONGE'])

    NEW_WORD6 = get_removed_words(['A-T-IL', 'ABATTU'], WORD6)
    assert WORD6[:9] == ['A-T-IL', 'ABAQUE', 'ABATEE', 'ABATTE',
                         'ABATTU', 'ABBAYE', 'ABCEDE', 'ABERRE', 'ABETIE']
    assert NEW_WORD6[:9] == ['ABAQUE', 'ABATEE', 'ABATTE',
                             'ABBAYE', 'ABCEDE', 'ABERRE', 'ABETIE', 'ABETIR', 'ABETIS']

    assert get_next_scales(['CHANGE', 'CHANTE'], WORD6) == [
        ['CHANGE', 'CHANTE', 'CHANCE'],
        ['CHANGE', 'CHANTE', 'CHANTA'],
        ['CHANGE', 'CHANTE', 'CHANTS'],
        ['CHANGE', 'CHANTE', 'CHARTE'],
        ['CHANGE', 'CHANTE', 'CHASTE'],
        ['CHANGE', 'CHANTE', 'CHATTE'],
        ['CHANGE', 'CHANTE', 'CRANTE']]

    t1 = perf_counter()
    print(' Result log :', get_scale(DICT_NAME, 'SUD', 'EST'))
    assert get_scale(DICT_NAME, 'SUD', 'EST') == ['SUD', 'SUT', 'EUT', 'EST']
    t2 = perf_counter()
    print(t2 - t1)
    # assert get_scale(DICT_NAME, 'HOMME', 'SINGE') ==  ['HOMME', 'COMME', 'COMTE', 'CONTE', 'CONGE',
    #                                                    'SONGE', 'SINGE']
    # t3 = perf_counter()
    # print(t3 - t2)
    # assert get_scale(DICT_NAME, 'EXOS', 'MATH') == ['EXOS', 'EROS', 'GROS', 'GRIS', 'GAIS', 'MAIS',
    #                                                 'MATS', 'MATH']
    # t4 = perf_counter()
    # print(t4 - t3)
    # assert get_scale(DICT_NAME, 'TOUT', 'RIEN') == ['TOUT', 'BOUT','BRUT', 'BRUN', 'BREN', 'BIEN', 'RIEN']
    # t5 = perf_counter()
    # print(t5 - t4)
    print("All tests OK")
