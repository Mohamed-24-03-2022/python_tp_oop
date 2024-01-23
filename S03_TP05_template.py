#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

# Une famille est représentée sous la forme d'une liste de personnes. Chaque personne est elle même représentée par
# un tuple qui aura la forme :
#   (num_id, nom, prénom, date_naissance, date_décès, num_sexe, métier, num_id_père, num_id_mère, num_id_conjoint)
#
# De plus les dates sont des tuples à 3 valeurs (num_jour, num_mois, num_année).
# Si la personne est encore vivante, sa date de décès est un tuple vide.
# Le num_sexe est 0 pour les femmes et de 1 pour les hommes.
# les num_id_XXX sont à 0 si l'information n'est pas pertinente ou inconnue.
# E.g : Dans ADAMS_FAMILY utilisée pour les test, l'arbre généalogique est le suivant :
#          Pierre -------------- Jeanne     André (RIP) -------------- Giselle
#           /           |            \                        |
#        Pierrot     Jeanette      Ginette --------------- Joseph
#
# L'objectif des 9 fonctions suivantes est d'extraire des informations en utilisant le plus possible
# les listes en compréhension du type [{map} for {var} in {sequence} {filter}] plutôt que des boucles.


def get_living(family):
    """ Retourne la liste de toutes les personnes vivantes de 'family'"""
    return [person for person in family if (not person[4])]


def get_gender_ranking(family):
    """ Retourne le 2-uplet correspondant aux femmes (resp. hommes) de 'family'"""
    return ([femme for femme in family if (not femme[5])], [homme for homme in family if (homme[5])])


def get_married_gender_proportion(family):
    """ Retourne le 2-uplet correspondant à la proportion femmes mariées / femmes (resp. hommes mariés / hommes)
    dans 'family'. Il faudra obligatoirement utiliser 'gender_ranking'."""
    family_ranked = get_gender_ranking(family)
    return tuple(3 / len(person) for person in family_ranked)


def get_death_age_average(family):
    """ Retourne la moyenne d'âge des décès dans la famille 'family' en ne considérant que l'année."""

    dead_persons_age = [person[4][2] - person[3][2]
                        for person in family if (person[4])]

    return sum(dead_persons_age) / len(dead_persons_age)


def get_age_average(family, year):
    """ Retourne la moyenne d'âge des personnes de 'family' encore vivantes l'année 'year' incluse"""

    dead_persons_by_this_year = [person for person in family if person[4]]
    alive_persons = get_living(family)

    dead_persons_age = [year - person[3][2]
                        for person in dead_persons_by_this_year if year >= person[3][2] and year <= person[4][2]]
    alive_persons_age = [year - person[3][2]
                         for person in alive_persons if year >= person[3][2]]

    length = len(dead_persons_age) + len(alive_persons_age)
    age_sum = sum(dead_persons_age) + sum(alive_persons_age)

    return age_sum / length


def get_deans(family):
    """ Retourne la liste des doyens de 'family' en ne tenant compte que de l'année de naissance"""
    return [dean for dean in get_living(family) if datetime.date.today().year - dean[3][2] >= 65]


def get_parents(ident, family):
    """ Retourne la liste des parents de la personne d'identifiant 'ident' dans 'family'"""
    pass


def is_intersecting(family1, family2):
    """ Retourne 'True' si 'family1' et 'family2' ont au moins un membre en commun. 'False' sinon."""
    pass


def is_sibling(id1, id2, family):
    """ Retourne 'True' si les personnes identifiées 'id1' et 'id2' ont au moins un parent en commun. False sinon.
    Il faudra obligatoirement utiliser 'intersect' et 'parents'."""
    pass


if __name__ == "__main__":
    DISTANCE_TEST = "ORANGE"
    ADAMS_FAMILY = [
        (1, "Dupond", "Pierre", (4, 6, 1949), (), 1, "physicien", 0, 0, 2),
        (2, "Dupond", "Jeanne", (7, 6, 1949), (), 0, "physicienne", 0, 0, 1),
        (3, "Dupond", "Pierrot", (7, 6, 1969), (), 1, "informaticien", 1, 2, 0),
        (4, "Dupond", "Jeannette", (5, 4, 1970), (), 0, "informaticienne", 1, 2, 0),
        (5, "Durand", "Ginette", (4, 3, 1972), (), 0, "chimiste", 1, 2, 8),
        (6, "Durand", "André", (6, 3, 1948), (7, 5, 1968), 1, "chimiste", 0, 0, 7),
        (7, "Durand", "Giselle", (7, 5, 1949), (), 0, "chimiste", 0, 0, 6),
        (8, "Durand", "Joseph", (3, 2, 1968), (), 1, "médecin", 6, 7, 5)]
    assert get_living(ADAMS_FAMILY) == [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                        (2, 'Dupond', 'Jeanne', (7, 6, 1949),
                                         (), 0, 'physicienne', 0, 0, 1),
                                        (3, 'Dupond', 'Pierrot', (7, 6, 1969),
                                         (), 1, 'informaticien', 1, 2, 0),
                                        (4, 'Dupond', 'Jeannette', (5, 4, 1970),
                                         (), 0, 'informaticienne', 1, 2, 0),
                                        (5, 'Durand', 'Ginette', (4, 3, 1972),
                                         (), 0, 'chimiste', 1, 2, 8),
                                        (7, 'Durand', 'Giselle', (7, 5, 1949),
                                         (), 0, 'chimiste', 0, 0, 6),
                                        (8, 'Durand', 'Joseph', (3, 2, 1968), (), 1, 'médecin', 6, 7, 5)]
    assert get_gender_ranking(ADAMS_FAMILY) == ([(2, 'Dupond', 'Jeanne', (7, 6, 1949), (), 0, 'physicienne', 0, 0, 1),
                                                 (4, 'Dupond', 'Jeannette', (5, 4, 1970),
                                                  (), 0, 'informaticienne', 1, 2, 0),
                                                 (5, 'Durand', 'Ginette', (4, 3, 1972),
                                                  (), 0, 'chimiste', 1, 2, 8),
                                                 (7, 'Durand', 'Giselle', (7, 5, 1949), (), 0, 'chimiste', 0, 0, 6)],
                                                [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                                 (3, 'Dupond', 'Pierrot', (7, 6, 1969),
                                                  (), 1, 'informaticien', 1, 2, 0),
                                                 (6, 'Durand', 'André', (6, 3, 1948),
                                                  (7, 5, 1968), 1, 'chimiste', 0, 0, 7),
                                                 (8, 'Durand', 'Joseph', (3, 2, 1968), (), 1, 'médecin', 6, 7, 5)])
    assert get_married_gender_proportion(ADAMS_FAMILY) == (0.75, 0.75)
    assert get_death_age_average(ADAMS_FAMILY) == 20.0
    assert get_age_average(ADAMS_FAMILY, 1967) == 18.25
    assert get_age_average(ADAMS_FAMILY, 1969) == 12.2
    assert get_deans(ADAMS_FAMILY) == [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                       (2, 'Dupond', 'Jeanne', (7, 6, 1949),
                                        (), 0, 'physicienne', 0, 0, 1),
                                       (7, 'Durand', 'Giselle', (7, 5, 1949), (), 0, 'chimiste', 0, 0, 6)]
    assert get_parents(3, ADAMS_FAMILY) == [(1, 'Dupond', 'Pierre', (4, 6, 1949), (), 1, 'physicien', 0, 0, 2),
                                            (2, 'Dupond', 'Jeanne', (7, 6, 1949), (), 0, 'physicienne', 0, 0, 1)]
    assert get_parents(8, ADAMS_FAMILY) == [
        (6, 'Durand', 'André', (6, 3, 1948), (7, 5, 1968), 1, 'chimiste', 0, 0, 7),
        (7, 'Durand', 'Giselle', (7, 5, 1949), (), 0, 'chimiste', 0, 0, 6)]
    assert not is_intersecting(get_living(ADAMS_FAMILY), [
                               p for p in ADAMS_FAMILY if p[4]])
    assert is_intersecting(get_living(ADAMS_FAMILY), get_deans(ADAMS_FAMILY))
    assert not is_sibling(6, 7, ADAMS_FAMILY)
    assert is_sibling(3, 4, ADAMS_FAMILY)
    assert is_sibling(3, 5, ADAMS_FAMILY)
    assert is_sibling(4, 5, ADAMS_FAMILY)
    assert not is_sibling(3, 6, ADAMS_FAMILY)
    print("All tests OK")
