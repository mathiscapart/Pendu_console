from getpass import getpass
import jeux
import wrd
import difficulty
import affichage


def select_mode():

    affichage.affichage()

    while True:
        diff = input(
            "Combien de vie vous voulez avoir 10 (rentrer 0), 5 (rentrer 1) ou 2 (rentrer 2)? "
        )

        try:
            assert len(diff) == 1
            diff = int(diff)
            assert diff == 0 or diff == 1 or diff == 2

        except ValueError:

            print("Vous n'avez pas choisis un nombre. \n")

        except AssertionError:

            print("Ce que vous avez rentrer ne correspond à aucune difficulter\n")

        else:
            break

    nombre_vie = difficulty.vie(diff)

    while True:
        mode = input(
            "Pour jouer contre l'ORDI rentrer 0 si vous voulez jouer JOUEUR contre JOUEUR rentrer 1: "
        )

        try:
            assert len(mode) == 1
            mode = int(mode)
            assert mode == 0 or mode == 1

        except ValueError:

            print("Vous n'avez pas choisis un nombre. \n")

        except AssertionError:

            print("Ce que vous avez rentrer ne correspond à aucune mode. \n")

        else:
            break

    if mode == 0:
        word = wrd.wrd()  # créer dans une variable le mot aléatoire
        cache = wrd.cacher(word)  # créer l'affichage type pendu
        jeux.jeux(cache, nombre_vie, word, diff)

    if mode == 1:
        word = getpass("Entrer le mot que vous voulez faire deviner: ").lstrip()
        for i in range(len(word)):
            while (
                word == "" or word[i] not in "abcdefghijklmnopqrstuvwxyz"
            ):  # vérifie si l'utilisateur rentre bien quelque chose
                word = getpass("Entrer un mot que vous voulez faire deviner: ").lstrip()

        cache = wrd.cacher(word)  # créer l'affichage type pendu
        jeux.jeux(cache, nombre_vie, word, diff)

    else:
        return
