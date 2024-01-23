# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
import chardet
import matplotlib.pyplot as plt


#########################################################################################################
# text from file names functions
#########################################################################################################

def get_text_from_file_name(file_name):
    """ retourne sous la forme d’une chaîne de caractères le texte du fichier de nom 'file_name' et encodé en utf8 """
    file_content = ""
    try:
        with open(file_name, 'r', encoding='utf-8') as f_out:
            file_content = f_out.read()
    except FileNotFoundError:
        print("File Not Found")
        return ""
    except Exception as e:
        print(e)
        return ""

    return file_content


def get_text_from_file_name_with_encoding(file_name):
    """ Détecte l’encodage du fichier de nom 'file_name' ouvert sous sa forme binaire puis retourne le dictionnaire
    des informations sur l’encodage détecté ainsi que le texte décodé sous la forme d’une chaîne de caractère.
    Vous utiliserez la fonction 'detect' du module 'chardet' et la fonction '.decode' associée aux chaînes binaires."""

    dict = {}
    file_content = ""
    try:
        with open(file_name, 'rb') as f_b_out:
            file_b_content = f_b_out.read()
            dict = chardet.detect(file_b_content)
        with open(file_name, 'r', encoding=dict["encoding"]) as f_out:
            file_content = f_out.read()
    except FileNotFoundError:
        print("File Not Found")
        return ""

    return dict, file_content


#########################################################################################################
# from alpha2 code functions
#########################################################################################################

def get_basic_alphabet(alpha2_code):
    """Retourne une chaîne constituée des caractères de la langue du pays dont le code sur 2 caractères est
    'alpha2_code'. Retourne "" si le code n’existe pas. Le chemin d'accès au fichier dans nos ressources est
    'PATH_ALPHABET + {alpha2_code}_alphabet.txt'. Vous capterez l'exception 'FileNotFoundError."""

    alphabet = get_text_from_file_name(
        PATH_ALPHABET + f"{alpha2_code}_alphabet.txt").split()

    return "".join(alphabet)


def get_diacriticals(alpha2_code):
    """ Retourne un dictionnaire constitué des paires associant les lettres susceptibles d’être accentuées (clés)
    et leur(s) homologue(s) avec l’accent (valeurs) dans la langue du pays dont le code sur 2 caractères est
    'alpha2_code'. Retourne '{}' si le code n’existe pas. Le chemin d'accès au fichier dans nos ressources est
    'PATH_ALPHABET + {alpha2_code}_diacriticals.txt'. Vous utiliserez 'str.join' et 'list.split'."""

    dict = {}
    alphabet_list = get_text_from_file_name(
        PATH_ALPHABET + f"{alpha2_code}_diacriticals.txt").split()
    for i, char in enumerate(alphabet_list):
        if (i % 2 == 0):
            special_char = alphabet_list[i+1].split("|")
            dict[char] = "".join(special_char)

    return dict


def get_accented_letters(alpha2_code):
    """ Retourne la chaîne des caractères accentués dans la langue du pays dont le code sur 2 caractères est
    'alpha2_code'. Retourne "" si le code n’est pas géré par nos ressources. Vous utiliserez les fonctions 'str.join',
    'dict.values', 'get_diacriticals' """
    res = ""
    dict = get_diacriticals(alpha2_code)
    letters_list = []
    for letter in dict:
        letters_list.append(dict[letter])
    res = "".join(letters_list)

    return res


def get_all_letters(alpha2_code):
    """ Retourne une chaîne constituée de toutes les lettres autorisées par la langue du pays dont le code sur 2
    caractères est 'alpha2_code'. Retourne "" si le code n’est pas géré par nos ressources. Vous utiliserez les
    fonctions 'get_basic_alphabet', 'get_accented_letter' et 'str.upper' """

    alphabet = get_basic_alphabet(
        alpha2_code) + get_accented_letters(alpha2_code)

    return alphabet + alphabet.upper().replace('&', '')


#########################################################################################################
# cleaning diacriticals functions
#########################################################################################################

def get_unaccented_letter(letter, diacriticals):
    """ Retourne le caractère 'letter'  mais sans les diacritiques du dictionnaire 'diacriticals' et sans changer la
    casse de caractère. Vous utiliserez les fonctions 'dict.items', 'str.lower' et 'str.upper'. """

    for charc in diacriticals:
        # if (charc.upper() == letter):
        #     return letter
        if (letter in diacriticals[charc].upper()):
            return charc.upper()

    return letter


def get_unaccented_text(text, diacriticals):
    """Retourne le texte de la chaîne 'text' mais sans les diacritiques du dictionnaire 'diacriticals' et sans changer
    la casse de caractère. Vous utiliserez 'get_unaccented_letter."""

    string_list = []
    upper_letters_index = []

    for i, letter in enumerate(text):
        if (letter.upper() == letter and letter.upper() != " " and letter.upper() != "!" and letter.upper() != "'" and letter.upper() != "."):
            upper_letters_index += [i]
        string_list.append(get_unaccented_letter(
            letter.upper(), diacriticals).lower())

    for i in upper_letters_index:
        string_list[i] = string_list[i].upper()

    return "".join(string_list)


#########################################################################################################
# character histogram functions
#########################################################################################################

def get_letters_histogram(text, alpha2_code):
    """ Retourne le dictionnaire des occurrences des lettres de 'text'. Tous le texte est d’abord mis en bas-de-casse
    et tous les diacritiques remplacés par leur homologue sans accent de la langue du pays dont le code sur 2 caractères
    est 'alpha2_code'. Vous devrez ensuite utiliser la définition en compréhension de dictionnaire et la fonction
    'str.count'."""

    res = {}

    text_unaccened_lowered = get_unaccented_text(
        text, get_diacriticals(alpha2_code)).lower()

    for letter in get_basic_alphabet(alpha2_code):
        res[letter] = text_unaccened_lowered.count(letter)

    return res


def get_normalized_histogram(histogram):
    """ Retourne 'histogram' en remplaçant pour chaque lettre le nombre d’occurrences par la valeur normalisée entre 0
    et 1 (arrondi au centième). """

    res = histogram.copy()
    somme = 0

    for letter in res:
        somme += res[letter]

    for letter in res:
        res[letter] = round((res[letter] / somme), 2)

    return res


def add_figure_histogram(figure_axis, histogram, is_sorted_by_freq=False):
    """Ajoute un diagramme à barre sur l’axe 'figure_axis' d’une figure 'matplotlib'. Ce diagramme représentera
    l’histogramme de caractères 'histogram'. Chaque barre représentera le nombre d’occurrences (axe des Y) des lettres
    (axe des Y). Selon la valeur booléenne de 'is_sorted_by_freq' les points seront ordonnées selon les valeurs
    croissantes des abscisses (False) ou selon les valeurs décroissantes des ordonnée (True). Vous utiliserez les
    fonctions 'dict.items' et 'list.sort' ou 'sorted' (en jouant avec ses paramètres 'key' et 'reverse'). """
    pass


if __name__ == "__main__":
    SENTENCE_TEST = "Bonne journée à tous et à toutes ! À tout à l'heure."
    LONG_TEXT_FILE_NAME_TEST = PATH_BOOKS + "FR/proust_swann.txt"
    DIACRITICALS = get_diacriticals('fr')
    assert get_text_from_file_name(
        PATH_DH + "ruDH.txt")[:20] == 'Всеобщая декларация '
    try:
        get_text_from_file_name(PATH_DH + "ruDH_source.txt")
    except UnicodeDecodeError as e:
        assert e.args[-1] == 'invalid start byte'
    finally:
        coding_info, decoded_text = get_text_from_file_name_with_encoding(
            PATH_DH + "ruDH_source.txt")
        assert coding_info == {'encoding': 'ISO-8859-5',
                               'confidence': 0.99, 'language': 'Russian'}
        assert decoded_text[:20] == 'Всеобщая декларация '
    assert get_basic_alphabet('fr') == 'abcdefghijklmnopqrstuvwxyzœæ&'
    assert get_basic_alphabet('en') == 'abcdefghijklmnopqrstuvwxyz&'
    assert get_basic_alphabet('ru') == ""
    assert get_diacriticals('fr') == {'a': 'àâä', 'e': 'éèêë', 'i': 'îï', 'o': 'ôö', 'u': 'ùûü', 'y': 'ÿ', 'c': 'ç',
                                      'n': 'ñ'}
    assert get_accented_letters('fr') == 'àâäéèêëîïôöùûüÿçñ'
    assert get_all_letters(
        'fr') == 'abcdefghijklmnopqrstuvwxyzœæ&àâäéèêëîïôöùûüÿçñABCDEFGHIJKLMNOPQRSTUVWXYZŒÆÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇÑ'
    assert get_unaccented_letter('E', DIACRITICALS) == 'E'
    assert get_unaccented_letter('È', DIACRITICALS) == 'E'
    assert get_unaccented_text(
        SENTENCE_TEST, DIACRITICALS) == "Bonne journee a tous et a toutes ! A tout a l'heure."
    assert get_letters_histogram(SENTENCE_TEST, 'fr') == {'a': 4, 'b': 1, 'c': 0, 'd': 0, 'e': 7, 'f': 0,
                                                          'g': 0, 'h': 1, 'i': 0, 'j': 1, 'k': 0, 'l': 1, 'm': 0,
                                                          'n': 3, 'o': 5, 'p': 0, 'q': 0, 'r': 2, 's': 2, 't': 6,
                                                          'u': 5, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'œ': 0,
                                                          'æ': 0, '&': 0}
    assert get_normalized_histogram(get_letters_histogram(SENTENCE_TEST, 'fr')) == {'a': 0.11, 'b': 0.03,
                                                                                    'c': 0.0, 'd': 0.0, 'e': 0.18,
                                                                                    'f': 0.0, 'g': 0.0, 'h': 0.03,
                                                                                    'i': 0.0, 'j': 0.03, 'k': 0.0,
                                                                                    'l': 0.03, 'm': 0.0, 'n': 0.08,
                                                                                    'o': 0.13, 'p': 0.0, 'q': 0.0,
                                                                                    'r': 0.05, 's': 0.05, 't': 0.16,
                                                                                    'u': 0.13, 'v': 0.0, 'w': 0.0,
                                                                                    'x': 0.0, 'y': 0.0, 'z': 0.0,
                                                                                    'œ': 0.0, 'æ': 0.0, '&': 0.0}
    # Attention l'instruction suivante prend au moins une dizaine de secondes
    assert get_letters_histogram(get_text_from_file_name(LONG_TEXT_FILE_NAME_TEST), 'fr') == {'a': 500865,
                                                                                              'b': 49082, 'c': 177328,
                                                                                              'd': 207558, 'e': 1008254,
                                                                                              'f': 59140, 'g': 47337,
                                                                                              'h': 43359, 'i': 434726,
                                                                                              'j': 38827, 'k': 433,
                                                                                              'l': 315158, 'm': 192400,
                                                                                              'n': 403399, 'o': 288434,
                                                                                              'p': 163221, 'q': 88647,
                                                                                              'r': 365815, 's': 449458,
                                                                                              't': 405115, 'u': 383183,
                                                                                              'v': 100792, 'w': 1914,
                                                                                              'x': 19715, 'y': 14034,
                                                                                              'z': 8044, 'œ': 0, 'æ': 1,
                                                                                              '&': 0}

    fig, ax = plt.subplots(3, 3, figsize=(15, 10))
    for col, code in zip(range(3), ['fr', 'en', 'pl']):
        ax[0][col].set_title(code + " (basic / sorted / normalized)")
        dh_text = get_text_from_file_name(PATH_DH + code + "DH.txt")
        hist = get_letters_histogram(dh_text, code)
        maxi = max(hist.values())
        ax[0][col].set_ylim(0, maxi)
        add_figure_histogram(ax[0][col], hist)
        ax[1][col].set_ylim(0, maxi)
        add_figure_histogram(ax[1][col], hist, True)
        ax[2][col].set_ylim(0, 1)
        add_figure_histogram(ax[2][col], get_normalized_histogram(hist), True)
    plt.show()
    print("All tests OK")
