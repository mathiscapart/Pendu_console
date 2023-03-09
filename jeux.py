from time import sleep
from timeit import default_timer as timer
import wrd
import difficulty


def jeux(cache, vie, word, diff):
    while True:
        skin = input(
            "Choississez votre personnage 0 pour homme, 1 pour femme, 2 pour Bugs Bunny: "
        )

        try:
            assert len(skin) == 1
            skin = int(skin)
            assert skin == 0 or skin == 1 or skin == 2

        except ValueError:

            print("Vous n'avez pas choisis un nombre. \n")

        except AssertionError:

            print("Votre proposition ne correspond à aucun personnage. \n")

        else:
            break

    print("Devinez le mot !")
    x = "_ "  # pour le while pour faire une boucle ça vérifie si il reste toujours des _ dans la variable cache
    lst = []  # liste des lettres qui sont déjà rentré

    try:  # si il y'a un problème il va renvoyer le problème
        start = timer()  # début de l'enregistrement du chrono
        while x in cache:  # boucle qui vérifie que le mot ne soit pas trouvé
            if vie > 0:  # vérifie si le joueur a toujours de la vie

                while True:
                    lettre = input(
                        "choississez une lettre: "
                    )  # demande une lettre au joueur
                    lettre = (
                        lettre.lower()
                    )  # fonction qui transforme la lettre en minuscule pour la manipuler plus facilement
                    try:
                        assert len(lettre) == 1
                        assert (
                            lettre in "abcdefghijklmnopqrstuvwxyz"
                        )  # vérifie si le joueur a bien rentré une lettre

                    except AssertionError:

                        print("Votre proposition ne correspond à aucune lettre. \n")

                    else:
                        break

                wrd.verification(lettre, lst)

                word = (
                    word.lower()
                )  # met le mot en miniscule pour le manipuler plus facilement

                for j in range(len(word)):
                    if lettre == word[j]:
                        cache[j] = word[j]

                if lettre not in word:
                    vie -= 1

                    if vie == 0:
                        difficulty.difficulte(diff, vie, skin)
                        print(
                            "Vous n'avez plus de vie.",
                            "\nVous avez perdu !!!",
                            f"\nle mot était {word}",
                        )
                        break

                    difficulty.difficulte(diff, vie, skin)
                    print(
                        f"Ce n'est pas la bonne lettre \nIl vous reste : {vie} vies\n"
                    )

                colle = "".join(cache)
                print(f"Il vous reste: {vie} vies \n{colle}\n")

        end = timer()

        if vie > 0:
            print(f"Bien joué.")
            sleep(2)
            print(
                f"VOUS AVEZ GAGNÉ !!!\nle mot était {word}\n"
                f"\nVous avez mis {round(end - start, 2)} secondes pour trouver le mot. BRAVOO!\n"
            )

    except BaseException as e:
        print(type(e), e)
