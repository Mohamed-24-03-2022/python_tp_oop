#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TP sur les types de base et les chaines de caractères
# Attention à bien réutiliser toute fonction déjà écrite si cela est pertinent.

def are_chars(chars, string):
    """ Retourne 'True' si tous les caractères 'chars' appartiennent la chaine 'string'.
    False sinon."""

    #! Method 1 sans l'operateur "in"
    # is_char_in_there = [False] * len(chars)

    # for i in range(len(chars)):
    #     if (chars[i] == ''):
    #         return False
    #     for j in range(len(string)):
    #         if (chars[i] == string[j]):
    #             is_char_in_there[i] = True

    # for res in is_char_in_there:
    #     if (res == False):
    #         return res
    # return True

    #! Method 2 avec l'operateur "in"
    for char in chars:
        if (char not in string):
            return False
    return True


# Les 3 fonctions suivantes simulent un brin d'ADN sous la forme d'une chaîne de caractères combinant les lettres
# A, T, G et C pour représenter les bases susceptibles de le composer. L'Adénine (A) est la base complémentaire de la
# Thymine (T) et la Guanine (G) est la complémentaire de la Cytozine (C). Les bases ont également une masse molaire :
# - A pèse 135 g/mol
# - T pèse 126 g/mol
# - G pèse 151 g/mol
# - C pèse 111 g/mol

def is_dna(dna):
    """ Retourne 'True' si le brin 'dna' contient uniquement des bases A, T, G ou C (et au moins une).
    'False' sinon. Il faudra utiliser la fonction 'are_chars'."""

    if (len(dna) == 0):
        return False

    return are_chars(dna.upper(), "ATGC")


def get_molar_mass(dna):
    """ Retourne 0 si dna n'est pas un brin. Sinon, retourne la masse molaire du brin 'dna'.
    Il faudra utiliser la fonction 'is_dna'."""

    if (not is_dna(dna)):
        return 0
    masse = 0
    for char in dna:
        if (char == 'A'):
            masse += 135
        if (char == 'T'):
            masse += 126
        if (char == 'G'):
            masse += 151
        if (char == 'C'):
            masse += 111
    return masse


def get_complementary(dna):
    """ Si 'dna' est un brin, retourne son complémentaire. Sinon retourne 'None'."""

    if (not is_dna(dna)):
        return None
    complementary = ''
    for char in dna:
        if (char == 'A'):
            complementary += 'T'
        if (char == 'T'):
            complementary += 'A'
        if (char == 'G'):
            complementary += 'C'
        if (char == 'C'):
            complementary += 'G'
    return complementary


# Les 4 fonctions suivantes permettent de jouer avec des mots


def get_first_deleted(char, string):
    """ Retourne la chaine 'string' amputée de la première occurrence du caractère 'char'"""

    for i in range(len(string)):
        if (char == string[i]):
            return string[0:i] + string[i+1:len(string)]
    return None


def is_scrabble(word, letters):
    """ Retourne True si le mot 'word' peut être construit comme au jeu du Scrabble à partir des lettres de la chaîne
    'letters' (les lettres répétées dans 'word' seront dont  également répétées au moins le même nombre de fois dans
    'letters'). False sinon. Il faudra obligatoirement utiliser 'get_first_deleted'."""

    for char in word:
        is_char_word_in_letters = get_first_deleted(char, letters)
        if (not is_char_word_in_letters):
            return False
    return True


def is_anagram(word1, word2):
    """ Retourne 'True' si 'word1' et 'word2' sont deux anagrammes.
    'False' sinon. Il faudra obligatoirement utiliser 'is_scrabble'."""

    return len(word1) == len(word2) and is_scrabble(word2, word1)


def get_hamming_distance(word1, word2):
    """ Retourne la distance de Hamming entre 'word1' et 'word2' ou -1 si son calcul n'est pas possible.
    La distance de Hamming entre deux chaines de même longueur correspond au nombre de positions auxquelles sont
    associés des caractères différents. """

    if (len(word1) != len(word2)):
        return -1

    hamming_distance = 0

    for i in range(len(word1)):
        if (word1[i] != word2[i]):
            hamming_distance += 1

    return hamming_distance


if __name__ == "__main__":
    DNA_TEST = 'GTATTCTCA'
    NOT_DNA_TEST = 'GTAITCTCA'
    WORDS1_TEST = "test"
    WORDS2_TEST = "tester"
    WORDS3_TEST = "est"
    SCRABBLE_TEST = "aeeigmnrrrstuwz"
    WORDS4_TEST = "marguerites"
    WORDS5_TEST = "rose"
    WORDS6_TEST = "gewurztraminers"

    assert are_chars(WORDS1_TEST, WORDS3_TEST)
    assert not are_chars(WORDS2_TEST, WORDS3_TEST)

    assert not is_dna('')
    assert is_dna(DNA_TEST)
    assert is_dna(DNA_TEST.lower())
    assert not is_dna(NOT_DNA_TEST)

    assert get_molar_mass('') == 0
    assert get_molar_mass(DNA_TEST) == 1147
    assert get_molar_mass(NOT_DNA_TEST) == 0

    assert get_complementary('') == None
    assert get_complementary(DNA_TEST) == 'CATAAGAGT'
    assert get_complementary(NOT_DNA_TEST) == None

    assert get_first_deleted('r', SCRABBLE_TEST) == 'aeeigmnrrstuwz'

    assert is_scrabble(WORDS4_TEST, WORDS6_TEST)
    assert not is_scrabble(WORDS5_TEST, WORDS6_TEST)

    assert is_anagram(WORDS6_TEST, SCRABBLE_TEST)
    assert not is_anagram(WORDS4_TEST, SCRABBLE_TEST)

    assert get_hamming_distance(WORDS6_TEST, SCRABBLE_TEST) == 13
    assert get_hamming_distance(WORDS4_TEST, SCRABBLE_TEST) == -1

    print("All tests OK")
