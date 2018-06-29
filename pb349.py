import time
import sys


class Problem():

    def __init__(self):
        self.orientation = (0, 1)  # (0,1) = haut (1,0) = droite (-1,0) = gauche (0,-1) = bas
        self.position = [50, 50]  # position actuelle de la fourmi  sur la grille
        self.compteur_de_noirs = 0  # compte le nombres de cases noires sur la grille
        self.compteur_des_etapes = 0  # nombre d'étapes déjà effectuées
        self.grille = [[True for i in range(100)]for j in range(100)]  # grille sur laquelle évolue la fourmi True =
        # blanc et False = noir
        self.couleur_derniere_position = True  # couleur de la position précédente après son changement de couleur
        self.liste_dernier_cycle = []  # dernier cycle de taille 104 rencontré, utilisée pour comparer avec le cycle en
        # cours pour vérifier si le motif qui se répète est atteint
        self.compteur_meme_cycle = 0  # nombre de fois successives où le dernier cycle était identique à celui en cours

    def tourner_sens_aiguilles(self, orientation_actuelle):  # fait tourner le vecteur orientation de 90° dans le sens
        # des aiguilles d'une montre
        return -orientation_actuelle[1], orientation_actuelle[0]

    def tourner_sens_contraire_aiguilles(self, orientation_actuelle):  # fait tourner le vecteur orientation de 90° dans
        #  le sens contraire des aiguilles d'une montre
        return orientation_actuelle[1], -orientation_actuelle[0]

    '''On sait que la fourmi après plus de environ  10 000 étapes suit un cycle régulier  de logueur 104. 
    Dans un premier temps je simule les 10 000 premières étapes, puis je simule par blocs de 104 jusqu\'a obtenir 3 fois
    de suite le meme cycle.  Plus de détails ici : https://en.wikipedia.org/wiki/Langton%27s_ant'''

    def simuler_une_etape(self):  # simule une étape de la fourmi en considérant la grille, la position de la fourmi et
        # sa direction
        couleur_position = self.grille[self.position[0]][self.position[1]]
        if couleur_position:
            nouvelle_direction = self.tourner_sens_aiguilles(self.orientation)
        else:
            nouvelle_direction = self.tourner_sens_contraire_aiguilles(self.orientation)
        nouvelle_position = list(map(sum, zip(self.position, nouvelle_direction)))  # additionne vectoriellement le
        # vecteur position et le vecteur direction
        self.grille[self.position[0]][self.position[1]] = not couleur_position  # on inverse la couleur dans la case
        # initiale
        if couleur_position:
            self.compteur_de_noirs += 1
        else:
            self.compteur_de_noirs -= 1
        self.position = nouvelle_position
        self.orientation = nouvelle_direction
        self.couleur_derniere_position = not couleur_position

    def simuler_10000(self):  # simule les 10 024 premières étapes, je choisis 10 024 car (10**18-10024) = 0 mod 104
        for i in range(10024):
            self.simuler_une_etape()
            self.compteur_des_etapes += 1

    def simuler_104(self):  # simule 104 étapes en stockant les résultats de chaque étapes pour pour pouvoir déterminer
        #  a posteriori si un cycle qui se répète est atteint
        cycle_en_cours = []
        for i in range(104):
            self.simuler_une_etape()
            self.compteur_des_etapes += 1
            cycle_en_cours.append(self.couleur_derniere_position)
        if self.liste_dernier_cycle == cycle_en_cours:
            self.compteur_meme_cycle += 1
        else:
            self.compteur_meme_cycle = 0
        self.liste_dernier_cycle = cycle_en_cours

    def obtenir_nombre_de_noirs_par_cycle(self):  # a partir de la liste du cycle donne le nombre de cases noires créées
        nombre_de_noirs_crees = 0
        for i in self.liste_dernier_cycle:
            if i:  # si la case est devenue blanche on a perdu une case noire
                nombre_de_noirs_crees -= 1
            else:  # si la case est devenue noire on a gagné une case blanche
                nombre_de_noirs_crees += 1
        return nombre_de_noirs_crees

    def get(self):
        self.simuler_10000()
        while self.compteur_meme_cycle < 3:
            self.simuler_104()
        etapes_restantes = 10**18 - self.compteur_des_etapes
        cycles_restants = etapes_restantes // 104  # etapes restantes est divisibles par 104 car 10**18 - 10 024 est
        # divisible par 104
        nombre_de_noirs_par_cycle = self.obtenir_nombre_de_noirs_par_cycle()
        self.compteur_de_noirs = self.compteur_de_noirs + (cycles_restants * nombre_de_noirs_par_cycle)

    def solve(self):
        self.get()
        print(self.compteur_de_noirs)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
