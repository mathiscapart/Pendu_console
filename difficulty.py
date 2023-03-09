import affichage_pendu


def difficulte(diff, vie, skin):
    if diff == 0:
        affichage_pendu.affichage_pendu_10(vie, skin)

    if diff == 1:
        affichage_pendu.affichage_pendu_5(vie, skin)

    if diff == 2:
        affichage_pendu.affichage_pendu_2(vie, skin)


def vie(diff):
    if diff == 0:
        vie = 10
        return int(vie)

    if diff == 1:
        vie = 5
        return int(vie)

    if diff == 2:
        vie = 2
        return int(vie)
