''' Ce module permet de jouer au jeu Tetris '''

from time import sleep
from random import randint
from graphisme import Fenetre
from modele import (Point,
                    PieceI, PieceO, PieceT, PieceJ, PieceL, PieceS, PieceZ,
                    Matrice,
                    Carre)


def main():
    """ Point d'entré du programme """

    def deplacer_piece(event):
        if event.keysym == 'Left':
            piece.deplacer_a_gauche(matrice_de_jeu)
        elif event.keysym == 'Right':
            piece.deplacer_a_droite(matrice_de_jeu)
        elif event.keysym == 'Down':
            piece.deplacer_vers_le_bas(matrice_de_jeu)


    pieces = [PieceI, PieceO, PieceT, PieceJ, PieceL, PieceS, PieceZ]

    fenetre_de_jeu = Fenetre()
    fenetre_de_jeu.get_fenetre().bind('<Key>', deplacer_piece)

    matrice_de_jeu = Matrice()

    # Choix aléatoire de la première pièce
    i = randint(0, 6)

    score = 0

    # On continu tant que la haut de la matrice n'est pas atteint
    while not any(matrice_de_jeu.get_haut_de_la_matrice()):

        # Choix aléatoire de la prochaine pièce
        j = randint(0, 6)

        fenetre_de_jeu.afficher_info_jeu(j, score, 0)

        piece = pieces[i]([Carre((Point(), Point()), 0, 0),
                           Carre((Point(), Point()), 0, 0),
                           Carre((Point(), Point()), 0, 0),
                           Carre((Point(), Point()), 0, 0)], 0)

        for i in range(4):
            piece.get_piece()[i].set_piece_du_carre(piece)

        matrice_de_jeu.ajouter_piece(piece)
        fenetre_de_jeu.afficher_matrice_de_jeu(matrice_de_jeu)

        fenetre_de_jeu.get_fenetre().bind('<Key>', deplacer_piece)

        while piece.deplacer_vers_le_bas(matrice_de_jeu):
            sleep(0.4)

            fenetre_de_jeu.afficher_matrice_de_jeu(matrice_de_jeu)

        score = matrice_de_jeu.update_matrice(fenetre_de_jeu)

        i = j

    fenetre_de_jeu.afficher_message_de_fin()
    fenetre_de_jeu.attendre_clic_x()



if __name__ == '__main__':
    main()
