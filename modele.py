'''
    Autheur: Allan Mouhani M. - Isty

    Représentation fonctionnelle du jeu.
'''

class Point():
    ''' Définition du type Point.'''

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        ''' retourne l'abscisse x'''
        return self.__x

    def get_y(self):
        ''' retourne l'ordonné y'''
        return self.__y

    def set_x(self, x__):
        ''' modifie la valeur de l'abscisse'''
        self.__x = x__

    def set_y(self, y__):
        ''' modifie la valeur de l'ordonnée'''
        self.__y = y__

##############################################################################

class Carre():
    ''' Définition du type Carré (couple de points)'''

    def __init__(self, points, ligne, colonne):
        self.__point1, self.__point2 = points
        self.__piece = None
        self.__canvas = None
        self.__id_canvas = None
        self.__ligne = ligne
        self.__colonne = colonne
        self.__decalage = 100
        self.__surface = 50

    def get_point_1(self):
        ''' retourne le premier point permettant de définir le carré'''
        return  self.__point1

    def get_point_2(self):
        ''' retourne le deuxième point permettant de définir le carré'''
        return self.__point2

    def get_ligne_matrice(self):
        ''' retourne la ligne dans la matrice, du carré en fonction de ces
            points'''
        return ((self.__point2.get_y() - self.__decalage)//self.__surface) - 1

    def get_colonne_matrice(self):
        ''' retourne la colonne dans la matrice, du carré en fonction de
            ces points '''
        return ((self.__point2.get_x() - self.__decalage)//self.__surface) - 1

    def get_piece_du_carre(self):
        ''' retourne la pièce à laquelle appartient le carré'''
        return self.__piece

    def get_canvas(self):
        ''' retourne la représentation graphique du carré '''
        return self.__canvas

    def get_canvas_id(self):
        ''' retourne l'identifiant graphique du carré '''
        return self.__id_canvas

    def set_ligne_matrice(self, ligne):
        ''' met à jour la ligne du carré ainsi que l'ordonné des points '''
        self.__ligne = ligne

        self.__point2.set_y(((ligne + 1) * self.__surface) + self.__decalage)
        self.__point1.set_y(self.__point2.get_y() - self.__surface)

    def set_colonne_matrice(self, colonne):
        ''' met à jour la colonne du carré,
            ainsi que l'abscisse des points '''
        self.__colonne = colonne

        self.__point2.set_x(((colonne + 1) * self.__surface) + self.__decalage)
        self.__point1.set_x(self.__point2.get_x() - self.__surface)

    def set_piece_du_carre(self, piece):
        ''' affecte le carré à une pièce'''
        self.__piece = piece

    def set_canvas(self, canvas):
        ''' ajoute un canvas(représentation graphique) au carré '''
        self.__canvas = canvas

    def set_canvas_id(self, id_canvas):
        ''' ajoute l'identifiant graphique du carré '''
        self.__id_canvas = id_canvas

    def enlever_de_la_matrice(self, matrice):
        ''' supprime le carré de la matrice passée en paramètre'''
        matrice[self.__ligne][self.__colonne] = None
        self.__canvas.delete(self.__id_canvas)

##############################################################################

class Piece():
    ''' Cette classe permet d'instancier des pièces(tetrominos)'''

    def __init__(self, piece, couleur, angle):
        self.__piece = piece
        self.__couleur = couleur
        self.__angle = angle

    def get_couleur_piece(self):
        ''' retourne la couleur de la pièce'''
        return self.__couleur

    def get_angle(self):
        ''' retourne l'angle de la pièce'''
        return self.__angle

    def get_piece(self):
        ''' retourne la pièce courante '''
        return self.__piece

    def set_angle(self, angle):
        ''' modifie l'angle de rotation de la pièce'''
        self.__angle = angle

    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''

    def pivoter(self, matrice):
        ''' fait pivoter la pièce'''

##############################################################################

class PieceI(Piece):
    ''' Cette classe permet d'instancier des pièces I '''

    def __init__(self, piece, angle):
        super().__init__(piece, 'cyan', angle)
        self.__piece = piece


    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''
        m__ = matrice.get_matrice()

        for i in range(4):
            colonne = self.__piece[i].get_colonne_matrice() - 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne < 0 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne - 1] = (None,
                                                                m__[ligne][colonne],
                                                                )
                self.__piece[i].set_colonne_matrice(colonne - 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), -50, 0)

            return True

        return False

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''
        m__ = matrice.get_matrice()

        for i in range(4):
            colonne = self.__piece[i].get_colonne_matrice() + 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne > 9 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne + 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 50, 0)

            return True

        return False

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''
        m__ = matrice.get_matrice()

        colonne = self.__piece[3].get_colonne_matrice()
        ligne = self.__piece[3].get_ligne_matrice() + 1

        if ligne > 15 or m__[ligne][colonne]:
            return False

        for i in range(3, -1, -1):
            ligne = self.__piece[i].get_ligne_matrice()
            colonne = self.__piece[i].get_colonne_matrice()

            m__[ligne][colonne], m__[ligne + 1][colonne] = (m__[ligne + 1][colonne],
                                                            m__[ligne][colonne])
            self.__piece[i].set_ligne_matrice(ligne + 1)

            if self.__piece[i].get_canvas():
                self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 0, 50)

        return True

    def pivoter(self, matrice):
        ''' fait pivoter la pièce'''
        m__ = matrice.get_matrice()

        if self.get_angle() == 0:

            l_1 = self.__piece[1].get_ligne_matrice()
            c_1 = self.__piece[1].get_colonne_matrice()

            if c_1 - 1 >= 0 and not m__[l_1][c_1 - 1]:
                m__[l_1][c_1 - 1] = self.__piece[0]

                l_2 = self.__piece[0].get_ligne_matrice()
                c_2 = self.__piece[0].get_colonne_matrice()







##############################################################################

class PieceO(Piece):
    ''' Cette classe permet d'instancier des pièces O '''

    def __init__(self, piece, angle):
        super().__init__(piece, 'yellow', angle)
        self.__piece = piece

    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''
        m__ = matrice.get_matrice()

        for i in range(0, 4, 2):
            colonne = self.__piece[i].get_colonne_matrice() - 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne < 0 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne - 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne - 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), -50, 0)

            return True

        return False

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''
        m__ = matrice.get_matrice()

        for i in range(1, 4, 2):
            colonne = self.__piece[i].get_colonne_matrice() + 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne > 9 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne + 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(),
                                                      50, 0)
            return True

        return False

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''
        m__ = matrice.get_matrice()

        for i in range(2, 4):
            colonne = self.__piece[i].get_colonne_matrice()
            ligne = self.__piece[i].get_ligne_matrice() + 1

            if ligne > 15 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne + 1][colonne] = (m__[ligne + 1][colonne],
                                                                m__[ligne][colonne])
                self.__piece[i].set_ligne_matrice(ligne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 0, 50)

            return True

        return False

##############################################################################

class PieceT(Piece):
    ''' Cette classe permet d'instancier des pièces T '''

    def __init__(self, piece, angle):
        super().__init__(piece, 'purple', angle)
        self.__piece = piece

    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''
        m__ = matrice.get_matrice()

        for i in range(0, 4, 3):
            colonne = self.__piece[i].get_colonne_matrice() - 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne < 0 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne - 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne - 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), -50, 0)

            return True

        return False

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''
        m__ = matrice.get_matrice()

        for i in range(2, 4):
            colonne = self.__piece[i].get_colonne_matrice() + 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne > 9 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne + 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(),
                                                      50, 0)
            return True

        return False

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''
        m__ = matrice.get_matrice()

        for i in range(4):
            if i == 1:
                continue
            colonne = self.__piece[i].get_colonne_matrice()
            ligne = self.__piece[i].get_ligne_matrice() + 1

            if ligne > 15 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne + 1][colonne] = (m__[ligne + 1][colonne],
                                                                m__[ligne][colonne])
                self.__piece[i].set_ligne_matrice(ligne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 0, 50)

            return True

        return False

##############################################################################

class PieceJ(Piece):
    ''' Cette classe permet d'instancier des pièces J '''

    def __init__(self, piece, angle):
        super().__init__(piece, 'blue', angle)
        self.__piece = piece

    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''
        m__ = matrice.get_matrice()

        for i in range(4):
            if i == 2:
                continue
            colonne = self.__piece[i].get_colonne_matrice() - 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne < 0 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                if i == 2:
                    continue
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne - 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne - 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), -50, 0)


            ligne = self.__piece[2].get_ligne_matrice()
            colonne = self.__piece[2].get_colonne_matrice()

            m__[ligne][colonne], m__[ligne][colonne - 1] = None, m__[ligne][colonne]
            self.__piece[2].set_colonne_matrice(colonne - 1)

            if self.__piece[2].get_canvas():
                self.__piece[2].get_canvas().move(self.__piece[2].get_canvas_id(), -50, 0)

            return True

        return False

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''
        m__ = matrice.get_matrice()

        for i in range(3):
            colonne = self.__piece[i].get_colonne_matrice() + 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne > 9 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne + 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 50, 0)

            return True

        return False

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''
        m__ = matrice.get_matrice()

        for i in range(2, 4):
            colonne = self.__piece[i].get_colonne_matrice()
            ligne = self.__piece[i].get_ligne_matrice() + 1

            if ligne > 15 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne + 1][colonne] = (m__[ligne + 1][colonne],
                                                                m__[ligne][colonne])
                self.__piece[i].set_ligne_matrice(ligne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 0, 50)

            return True

        return False

##############################################################################

class PieceL(Piece):
    ''' Cette classe permet d'instancier des pièces J '''

    def __init__(self, piece, angle):
        super().__init__(piece, 'orange red', angle)
        self.__piece = piece

    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''
        m__ = matrice.get_matrice()

        for i in range(3):
            colonne = self.__piece[i].get_colonne_matrice() - 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne < 0 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne - 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne - 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), -50, 0)

            return True

        return False

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''
        m__ = matrice.get_matrice()

        for i in range(4):
            if i == 2:
                continue
            colonne = self.__piece[i].get_colonne_matrice() + 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne > 9 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne + 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(),
                                                      50, 0)
            return True

        return False

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''
        m__ = matrice.get_matrice()

        for i in range(2, 4):
            colonne = self.__piece[i].get_colonne_matrice()
            ligne = self.__piece[i].get_ligne_matrice() + 1

            if ligne > 15 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne + 1][colonne] = (m__[ligne + 1][colonne],
                                                                m__[ligne][colonne])
                self.__piece[i].set_ligne_matrice(ligne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 0, 50)

            return True

        return False

##############################################################################

class PieceS(Piece):
    ''' Cette classe permet d'instancier des pièces S '''

    def __init__(self, piece, angle):
        super().__init__(piece, 'green', angle)
        self.__piece = piece


    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''
        m__ = matrice.get_matrice()

        for i in range(0, 4, 2):
            colonne = self.__piece[i].get_colonne_matrice() - 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne < 0 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne - 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne - 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), -50, 0)

            return True

        return False

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''
        m__ = matrice.get_matrice()

        for i in range(1, 4, 2):
            colonne = self.__piece[i].get_colonne_matrice() + 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne > 9 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne + 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(),
                                                      50, 0)
            return True

        return False

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''
        m__ = matrice.get_matrice()

        for i in range(1, 4):
            colonne = self.__piece[i].get_colonne_matrice()
            ligne = self.__piece[i].get_ligne_matrice() + 1

            if ligne > 15 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne + 1][colonne] = (m__[ligne + 1][colonne],
                                                                m__[ligne][colonne])
                self.__piece[i].set_ligne_matrice(ligne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 0, 50)

            return True

        return False

##############################################################################

class PieceZ(Piece):
    ''' Cette classe permet d'instancier des pièces Z '''

    def __init__(self, piece, angle):
        super().__init__(piece, 'red', angle)
        self.__piece = piece

    def deplacer_a_gauche(self, matrice):
        ''' déplace la pièce sur la gauche '''
        m__ = matrice.get_matrice()

        for i in range(0, 4, 2):
            colonne = self.__piece[i].get_colonne_matrice() - 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne < 0 or m__[ligne][colonne]:
                break
        else:
            for i in range(4):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne - 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne - 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), -50, 0)

            return True

        return False

    def deplacer_a_droite(self, matrice):
        ''' déplace la pièce sur la droite '''
        m__ = matrice.get_matrice()

        for i in range(1, 4, 2):
            colonne = self.__piece[i].get_colonne_matrice() + 1
            ligne = self.__piece[i].get_ligne_matrice()

            if colonne > 9 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne][colonne + 1] = None, m__[ligne][colonne]
                self.__piece[i].set_colonne_matrice(colonne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(),
                                                      50, 0)
            return True

        return False

    def deplacer_vers_le_bas(self, matrice):
        ''' déplace la pièce vers le bas '''
        m__ = matrice.get_matrice()

        for i in range(4):
            if i == 1:
                continue
            colonne = self.__piece[i].get_colonne_matrice()
            ligne = self.__piece[i].get_ligne_matrice() + 1

            if ligne > 15 or m__[ligne][colonne]:
                break
        else:
            for i in range(3, -1, -1):
                ligne = self.__piece[i].get_ligne_matrice()
                colonne = self.__piece[i].get_colonne_matrice()

                m__[ligne][colonne], m__[ligne + 1][colonne] = (m__[ligne + 1][colonne],
                                                                m__[ligne][colonne])
                self.__piece[i].set_ligne_matrice(ligne + 1)

                if self.__piece[i].get_canvas():
                    self.__piece[i].get_canvas().move(self.__piece[i].get_canvas_id(), 0, 50)

            return True

        return False

##############################################################################

class Matrice():
    ''' Représentation du plateau de jeu par une matrice 16x10 '''

    def __init__(self):
        self.__matrice = [[None for i in range(10)] for j in range(16)]

    def get_nombre_de_ligne(self):
        ''' retourne le nombre de ligne de la matrice'''
        return len(self.__matrice)

    def get_nombre_de_colonne(self):
        ''' retoune le nombre de colonne de la matrice'''
        return len(self.__matrice[0])

    def get_carre(self, ligne, colonne):
        ''' retourne le carre se trouvant à [ligne][colonne]
        '''
        return self.__matrice[ligne][colonne]

    def get_matrice(self):
        ''' retourne la matrice de jeu (plateau) '''
        return self.__matrice

    def get_haut_de_la_matrice(self):
        ''' retourne la première ligne de la matrice.
            Utile pour tester la fin de partie.'''
        return self.__matrice[0]

    def __ajouter_piece_i(self, piece_i):
        ''' ajoute une pièce I dans la matrice'''
        ligne = 0
        colonne = 5

        for i in range(4):
            if not self.__matrice[ligne][colonne]:
                piece_i.get_piece()[i].set_ligne_matrice(ligne)
                piece_i.get_piece()[i].set_colonne_matrice(colonne)
                self.__matrice[ligne][colonne] = piece_i.get_piece()[i]
                ligne += 1
            else:
                break    

    def __ajouter_piece_o(self, piece_o):
        ''' ajoute une pièce O dans la matrice'''

        ligne = 0
        colonne = 5

        for i in range(0, 4, 2):
            piece_o.get_piece()[i].set_ligne_matrice(ligne)
            piece_o.get_piece()[i].set_colonne_matrice(colonne)

            piece_o.get_piece()[i + 1].set_ligne_matrice(ligne)
            piece_o.get_piece()[i + 1].set_colonne_matrice(colonne + 1)

            self.__matrice[ligne][colonne] = piece_o.get_piece()[i]
            self.__matrice[ligne][colonne + 1] = piece_o.get_piece()[i + 1]
            ligne += 1

    def __ajouter_piece_t(self, piece_t):
        ''' ajoute une pièce T dans la matrice'''

        ligne = 0
        colonne = 4

        for i in range(3):
            piece_t.get_piece()[i].set_ligne_matrice(ligne)
            piece_t.get_piece()[i].set_colonne_matrice(colonne)

            self.__matrice[ligne][colonne] = piece_t.get_piece()[i]
            colonne += 1

        piece_t.get_piece()[3].set_ligne_matrice(1)
        piece_t.get_piece()[3].set_colonne_matrice(5)

        self.__matrice[1][5] = piece_t.get_piece()[3]

    def __ajouter_piece_j(self, piece_j):
        ''' ajoute une pièce J dans la matrice'''

        ligne = 0
        colonne = 5

        for i in range(3):
            piece_j.get_piece()[i].set_ligne_matrice(ligne)
            piece_j.get_piece()[i].set_colonne_matrice(colonne)
            self.__matrice[ligne][colonne] = piece_j.get_piece()[i]
            ligne += 1

        piece_j.get_piece()[3].set_ligne_matrice(2)
        piece_j.get_piece()[3].set_colonne_matrice(4)

        self.__matrice[2][4] = piece_j.get_piece()[3]

    def __ajouter_piece_l(self, piece_l):
        ''' ajoute une pièce L dans la matrice'''
        ligne = 0
        colonne = 5

        for i in range(3):
            piece_l.get_piece()[i].set_ligne_matrice(ligne)
            piece_l.get_piece()[i].set_colonne_matrice(colonne)
            self.__matrice[ligne][colonne] = piece_l.get_piece()[i]
            ligne += 1

        piece_l.get_piece()[3].set_ligne_matrice(2)
        piece_l.get_piece()[3].set_colonne_matrice(6)
        self.__matrice[2][6] = piece_l.get_piece()[3]

    def __ajouter_piece_s(self, piece_s):
        ''' ajoute une pièce S dans la matrice'''

        ligne = 0
        colonne = 5

        for i in range(0, 4, 2):
            piece_s.get_piece()[i].set_ligne_matrice(ligne)
            piece_s.get_piece()[i].set_colonne_matrice(colonne)

            piece_s.get_piece()[i + 1].set_ligne_matrice(ligne)
            piece_s.get_piece()[i + 1].set_colonne_matrice(colonne + 1)

            self.__matrice[ligne][colonne] = piece_s.get_piece()[i]
            self.__matrice[ligne][colonne + 1] = piece_s.get_piece()[i + 1]

            ligne += 1
            colonne -= 1

    def __ajouter_piece_z(self, piece_z):
        ''' ajoute une pièce Z dans la matrice'''
        ligne = 0
        colonne = 5

        for i in range(0, 4, 2):
            piece_z.get_piece()[i].set_ligne_matrice(ligne)
            piece_z.get_piece()[i].set_colonne_matrice(colonne)

            piece_z.get_piece()[i + 1].set_ligne_matrice(ligne)
            piece_z.get_piece()[i + 1].set_colonne_matrice(colonne + 1)

            self.__matrice[ligne][colonne] = piece_z.get_piece()[i]
            self.__matrice[ligne][colonne + 1] = piece_z.get_piece()[i + 1]

            ligne += 1
            colonne += 1

    def ajouter_piece(self, piece):
        ''' Ajoute une pièce dans la matrice '''
        if isinstance(piece, PieceI):
            self.__ajouter_piece_i(piece)
        elif isinstance(piece, PieceO):
            self.__ajouter_piece_o(piece)
        elif isinstance(piece, PieceT):
            self.__ajouter_piece_t(piece)
        elif isinstance(piece, PieceJ):
            self.__ajouter_piece_j(piece)
        elif isinstance(piece, PieceL):
            self.__ajouter_piece_l(piece)
        elif isinstance(piece, PieceS):
            self.__ajouter_piece_s(piece)
        else:
            self.__ajouter_piece_z(piece)

    def update_matrice(self, fenetre_de_jeu):
        ''' permet de mettre à jour la matrice , notamment en supprimant
            les lignes pleines.'''
        score = 0

        # On part du bas de la matrice
        for i in range(self.get_nombre_de_ligne() - 1, -1, -1):
            while all(self.__matrice[i]):
                for j in range(self.get_nombre_de_colonne()):
                    carre = self.__matrice[i][j].enlever_de_la_matrice(self.__matrice)
                    del carre
                fenetre_de_jeu.afficher_matrice_de_jeu(self)
                score += 1

                if i - 1 >= 0:
                    for k in range(i - 1, -1, -1):
                        for j in range(10):
                            carre = self.__matrice[k][j]
                            if carre:
                                # On fait descendre les pièces tant que cela est possible
                                while True:
                                    colonne = carre.get_colonne_matrice()
                                    ligne = carre.get_ligne_matrice() + 1

                                    if ligne > 15 or self.__matrice[ligne][colonne]:
                                        break
                                    else:
                                        self.__matrice[ligne][colonne] = carre
                                        self.__matrice[ligne - 1][colonne] = None
                                        carre.set_ligne_matrice(ligne)

                                        if carre.get_canvas():
                                            carre.get_canvas().move(carre.get_canvas_id(), 0, 50)
                fenetre_de_jeu.afficher_matrice_de_jeu(self)

        return score


if __name__ == '__main__':

    matrice_de_jeu = Matrice()

    #pieces = [PieceI, PieceO, PieceT, PieceJ, PieceL, PieceS, PieceZ]

    print(matrice_de_jeu.get_matrice(), "\n\n\n")


    PIECE__ = PieceO([Carre((Point(), Point()), 0, 0),
                      Carre((Point(), Point()), 0, 0),
                      Carre((Point(), Point()), 0, 0),
                      Carre((Point(), Point()), 0, 0)], 0)

    matrice_de_jeu.ajouter_piece(PIECE__)
    print(matrice_de_jeu.get_matrice(), "\n\n\n")

    for index in range(4):
        PIECE__.get_piece()[index].set_piece_du_carre(PIECE__)

    while PIECE__.deplacer_a_gauche(matrice_de_jeu):
        print(matrice_de_jeu.get_matrice(), "\n\n\n")
