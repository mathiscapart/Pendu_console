from random import choice


def wrd():
    with open("liste.de.mots.francais.sansaccents.txt", "r") as f:
        line = f.readlines()
        word = choice(line).strip()
    return word


def cacher(word):
    cacher = []
    for i in range(1, len(word) + 1):
        cacher.append("_ ")
    return cacher


def verification(lettre, lst):
    while lettre in lst:
        print("Vous avez déjà entrer cette lettre.")
        lettre = input("choississez une lettre: ")
    if lettre not in lst:
        lst += lettre
    return lettre
