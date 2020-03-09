'''Ce module permet de gérer la partie graphique du jeu '''

from time import sleep
import tkinter

class Fenetre():
    ''' permet d'instancier des objets représentant
        une fenêtre de jeu '''

    def __init__(self):
        self.__fenetre = tkinter.Tk()
        self.__configurer_fenetre()

        self.__score_id = None
        self.__score = 0

        self.__niveau_id = None
        self.__niveau = 0

        self.__canvas_pieces = [[None, 'cyan'], [None, 'yellow'],
                                [None, 'purple'], [None, 'blue'],
                                [None, 'orange red'], [None, 'green'],
                                [None, 'red']]

        self.__ajouter_quadrillage()
        self.__ajouter_canvas_pieces()

    def __configurer_fenetre(self):
        ''' permet de configurer la fenêtre de jeu, en modifiant notamment :
            le titre de la fenêtre, ses dimensions ... '''

        self.__fenetre.title('Tetris')
        self.__fenetre.geometry('800x950')
        self.__fenetre.resizable(False, False)


    def attendre_clic_x(self):
        ''' Ferme la fenêtre de jeu lorsque l'utilisateur clique sur X '''
        self.__fenetre.mainloop()

    def __ajouter_quadrillage(self):
        ''' ajoute un quadrillage à la fenêtre de jeu '''
        self.__canvas = tkinter.Canvas(self.__fenetre, width=800, height=950,
                                       bg='black')
        self.__rect = self.__canvas.create_rectangle(100, 100, 600, 900,
                                                     width=10, outline='blue',
                                                     fill='gray17')

        x_1, y_1, x_2, y_2 = 150, 100, 150, 900

        for _ in range(9):
            self.__canvas.create_line(x_1, y_1, x_2, y_2, fill="white")
            x_1 += 50
            x_2 += 50

        x_1, y_1, x_2, y_2 = 100, 150, 600, 150

        for _ in range(15):
            self.__canvas.create_line(x_1, y_1, x_2, y_2, fill="white")
            y_1 += 50
            y_2 += 50

        self.__score_id = self.__canvas.create_text(700, 50,
                                                    text='Score : {}'.format(self.__score),
                                                    font=('Helvetica'), fill='white',
                                                    activefill='indianred1')

        self.__niveau_id = self.__canvas.create_text(700, 100,
                                                     text='Niveau : {}'.format(self.__niveau),
                                                     font=('Helvetica'), fill='white',
                                                     activefill='indianred1')

        self.__canvas.create_text(710, 200, text='Prochain : ',
                                  font=('Helvetica'), fill='white',
                                  activefill='indianred1')

        self.__canvas.pack()


    def __ajouter_canvas_piece_i(self):
        ''' ajoute une représentation graphique d'une pièce I.
            Utiliser pour l'affichage de la prochine pièce '''

        x_1, y_1, x_2, y_2 = 671, 246, 689, 350

        self.__canvas_pieces[0][0] = []
        canvas_i = self.__canvas_pieces[0][0]
        canvas_i.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

    def __ajouter_canvas_piece_o(self):
        ''' ajoute une représentation graphique d'une pièce O.
            Utiliser pour l'affichage de la prochine pièce '''

        x_1, y_1, x_2, y_2 = 610, 220, 670, 280

        self.__canvas_pieces[1][0] = []
        canvas_o = self.__canvas_pieces[1][0]
        canvas_o.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

    def __ajouter_canvas_piece_t(self):
        ''' ajoute une représentation graphique d'une pièce T.
            Utiliser pour l'affichage de la prochine pièce '''

        x_1, y_1, x_2, y_2 = 610, 281, 670, 306

        self.__canvas_pieces[2][0] = []
        canvas_t = self.__canvas_pieces[2][0]

        canvas_t.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

        x_1, y_1, x_2, y_2 = 630, 306, 650, 331

        canvas_t.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))


    def __ajouter_canvas_piece_j(self):
        ''' ajoute une représentation graphique d'une pièce J.
            Utiliser pour l'affichage de la prochine pièce '''

        x_1, y_1, x_2, y_2 = 766, 270, 791, 335

        self.__canvas_pieces[3][0] = []
        canvas_j = self.__canvas_pieces[3][0]
        canvas_j.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

        x_1, y_1, x_2, y_2 = 741, 315, 766, 335

        canvas_j.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

    def __ajouter_canvas_piece_l(self):
        ''' ajoute une représentation graphique d'une pièce L.
            Utiliser pour l'affichage de la prochine pièce '''

        x_1, y_1, x_2, y_2 = 690, 260, 715, 335

        self.__canvas_pieces[4][0] = []
        canvas_l = self.__canvas_pieces[4][0]
        canvas_l.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

        x_1, y_1, x_2, y_2 = 715, 315, 740, 335

        canvas_l.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

    def __ajouter_canvas_piece_s(self):
        ''' ajoute une représentation graphique d'une pièce S.
            Utiliser pour l'affichage de la prochine pièce '''

        x_1, y_1, x_2, y_2 = 750, 220, 790, 245

        self.__canvas_pieces[5][0] = []
        canvas_j = self.__canvas_pieces[5][0]
        canvas_j.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

        x_1, y_1, x_2, y_2 = 732, 245, 772, 270

        canvas_j.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))


    def __ajouter_canvas_piece_z(self):
        ''' ajoute une représentation graphique d'une pièce Z.
            Utiliser pour l'affichage de la prochine pièce '''

        x_1, y_1, x_2, y_2 = 671, 220, 711, 245

        self.__canvas_pieces[6][0] = []
        canvas_j = self.__canvas_pieces[6][0]
        canvas_j.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

        x_1, y_1, x_2, y_2 = 691, 245, 731, 270

        canvas_j.append(self.__canvas.create_rectangle(x_1,
                                                       y_1, x_2, y_2))

    def __ajouter_canvas_pieces(self):
        ''' ajoute toutes les représentations graphiques des différentes
            pièces '''
        self.__ajouter_canvas_piece_i()
        self.__ajouter_canvas_piece_o()
        self.__ajouter_canvas_piece_t()
        self.__ajouter_canvas_piece_j()
        self.__ajouter_canvas_piece_l()
        self.__ajouter_canvas_piece_s()
        self.__ajouter_canvas_piece_z()


    def afficher_info_jeu(self, id_piece, score=0, niveau=0):
        ''' affiche des infos sur le jeu dont le score
            ainsi que la prochaine pièce '''

        if score:
            self.__score += score
            self.__canvas.itemconfig(self.__score_id,
                                     text='Score : {}'.format(self.__score))
        if niveau:
            self.__niveau += niveau
            self.__canvas.itemconfig(self.__niveau_id,
                                     text='Score : {}'.format(self.__niveau))

        couleur = self.__canvas_pieces[id_piece][1]
        canvas = self.__canvas_pieces[id_piece][0]

        for i in range(7):
            if i != id_piece and self.__canvas_pieces[i][0]:
                if i in (0, 1):
                    self.__canvas.itemconfig(self.__canvas_pieces[i][0],
                                             fill='black')
                else:
                    for j in range(2):
                        self.__canvas.itemconfig(self.__canvas_pieces[i][0][j],
                                                 fill='black')

        if id_piece in (0, 1):
            self.__canvas.itemconfig(canvas, fill=couleur)
        else:
            for i in range(2):
                self.__canvas.itemconfig(canvas[i], fill=couleur)


    def afficher_matrice_de_jeu(self, matrice):
        ''' affiche la matrice de jeu'''
        m__ = matrice.get_matrice()

        for i in range(matrice.get_nombre_de_ligne()):
            for j in range(matrice.get_nombre_de_colonne()):
                if m__[i][j] and not m__[i][j].get_canvas():
                    x_1 = m__[i][j].get_point_1().get_x()
                    y_1 = m__[i][j].get_point_1().get_y()

                    x_2 = m__[i][j].get_point_2().get_x()
                    y_2 = m__[i][j].get_point_2().get_y()

                    couleur = m__[i][j].get_piece_du_carre().get_couleur_piece()
                    m__[i][j].set_canvas(self.__canvas)
                    m__[i][j].set_canvas_id(self.__canvas.create_rectangle(x_1, y_1,
                                                                           x_2, y_2,
                                                                           fill=couleur))

        self.__fenetre.update()

    def afficher_message_de_fin(self):
        ''' affiche le message de fin de jeu'''

        m__ = self.__canvas.create_text(400, 400, text='GAME OVER',
                                        font=('Helvetica', 70, 'bold italic'),
                                        fill='indianred1', activefill='white')


    def get_fenetre(self):
        ''' retourne la fenêtre de jeu courante '''
        return self.__fenetre


if __name__ == '__main__':
    fenetre_principale = Fenetre()

    fenetre_principale.attendre_clic_x()
