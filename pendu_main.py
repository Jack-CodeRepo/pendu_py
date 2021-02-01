#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================
"""
    Jeu du pendu

    Usage:
        pendu_main.py <play>
        pendu_main.py (-h | --help)
        pendu_main.py (-v | --version)

    Argument
        <play>:         Renseigner "play" afin de jouer.


    Options:
        -h --help       Affiche cet écran.
        -v --version    Afficher la version.

"""

# ==================================================================================================
#   IMPORT
# ==================================================================================================

# import framework GUI tkinter
import tkinter as tk

# import module standard python
import random
import json
import docopt

# import liste
from lists import words

# import des éléments modifiables
import classes.elements.player  as playerCls
import classes.elements.mot     as motCls
import classes.elements.lettre  as lettreCls

# import des composants d'interface
import classes.interface.menu_bar   as menu_bar
import classes.interface.bouton     as bouton
import classes.interface.saisie     as saisie
import classes.interface.display    as display



# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================

# fichier de sauvegarde
save_file = "misc/players.json"
# attribution de la liste des mots à deviner en variable
words_list = words.MHWI



# ==================================================================================================
#   OBJETS
# ==================================================================================================

joueur = playerCls.class_player()
mot_visible = motCls.class_mot()
mot_cache = motCls.class_mot()
lettre = lettreCls.class_lettre()



# ==================================================================================================
#   PLAYERS JSON
# ==================================================================================================

with open(save_file, 'r') as f:
    data_players = json.load(f)



# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

def write_json():
    """
    Ecris les données dans le fichier .json de sauvegarde.
    Il n'est nécessaire de spécifier le fichier en argument car un seul fichier est utilisé.
    """
    with open(save_file, "w") as f:
        json.dump(data_players, f, indent=4)



def get_score(playerName):
    """
    Récupère le score du joueur

    Args:
        playerName (string): nom du joueur ciblé

    Returns:
        int: score du joueur ciblé
    """
    score = data_players["players"][playerName]
    return score



def add_player(playerName):
    """
    Ajoute le joueur

    Args:
        playerName (string): nom du joueur à ajouter
    """
    score = "10"
    added_data = {playerName: score}
    temp = data_players["players"]
    temp.update(added_data)

    write_json()



def delete_player(playerName):
    """
    Supprime le joueur

    Args:
        playerName (string): nom du joueur à supprimer
    """
    pName = playerName.lower()
    if pName in data_players["players"]:
        del data_players["players"][pName]

        write_json()



def check_player(playerName):
    """
    Vérifie si le joueur existe dans le .json de sauvegarde
    Si le joueur n'existe pas, rajoute le joueur dans le .json de sauvegarde
    Initialise certains attributs de l'objet "joueur"

    Args:
        playerName (string): nom du joueur
    """
    if playerName in data_players["players"]:
        joueur.set_name(playerName)
        joueur.set_score(get_score(playerName))
    else:
        add_player(playerName)
        joueur.set_name(playerName)
        joueur.set_score(get_score(playerName))



def update_score(playerName, score):
    """
    met à jour le score du joueur dans le fichier .json de sauvegarde

    Args:
        playerName (string): nom du joueur
        score (int): score du joueur
    """
    if playerName in data_players["players"]:
        data_players["players"][playerName] = score

    write_json()



def check_lettre():
    """
    Vérifie la lettre
    Si un des caractère dans le mot à deviner est "-", alors il est ajouté

    Returns:
        string: le mot caché mis à jour si la lettre est trouvée
    """
    l = lettre.get_name()
    m = mot_visible.get_name()
    mc = mot_cache.get_name()

    mc_list = []
    mc_display_list = []

    if not mc:
        mc = hide_word(m)

    for i in range(len(m)):
        if l == m[i]:
            mc_list.append(l)
        elif mc[i].isalpha():
            mc_list.append(mc[i])
        elif m[i] == "-":
            mc_list.append("-")
        else:
            mc_list.append("_")

    if l not in m:
        mot_visible.lower_tentative(1)

    mc = "".join(mc_list)
    mot_cache.set_name(mc)

    for i in mc:
        mc_display_list.append(i+" ")
    
    mc_display = "".join(mc_display_list)
    string = f"{mc_display}"
    return string



def check_score(playerName):
    """
    Vérifie le score et renvois une string contenant un message

    Args:
        playerName (string): nom du joueur avec lequel vérifier le score

    Returns:
        string: une string contenant un message approprié
    """
    string_output = ""
    tentative = mot_visible.get_tentative()

    # si toutes les lettres sont trouvees
    if "_" not in mot_cache.get_name():
        joueur.increase_score(5)
        update_score(playerName, joueur.get_score())
        string_output = f"Félicitations! Vous avez gagné! Votre score est de {joueur.get_score()}"

    else:
        # si il n'y a plus de tentative
        if tentative == 0:
            joueur.lower_score(2)
            update_score(playerName, joueur.get_score())
            string_output = f"Il vous reste {tentative} tentative, vous avez perdu."

        else:
            string_output = f"Il vous reste {tentative} tentatives."

    # si le score total du joueur est à zéro
    if joueur.get_score() == 0:
        delete_player(playerName)
        string_output = f"Vous avez {joueur.get_score()} en score. \n Votre sauvegarde a été supprimée."

    return string_output



def hide_word(word):
    """remplace chaque charactere d'une string par "_ "

    Args:
        word (string): string à transformer

    Returns:
        string: string transformée
    """
    mot = []
    mot_long = len(word)
    for i in range(mot_long):
        mot.insert(i, "_")
    return mot



def pick_random_word(list_word):
    """choisi un mot aléatoire à partir d'une liste de string, et le renvois

    Args:
        list_word (liste): liste dans laquelle choisir

    Returns:
        string: mot choisi parmis la liste
    """

    word = random.choice(list_word)
    return str(word).upper()



def affichage(objet, liste):
    """affiche les éléments dans la GUI

    Args:
        objet (tkinter.Text):   objet gérant l'endroit où afficher (l'objet doit etre créé avec la classe display)
        liste (list,string):    string ou liste des éléments à afficher
    """

    if type(liste) is list:
        objet.config(state=tk.NORMAL, font="Calibri")
        objet.delete('1.0', tk.END)
        for l in liste:
            objet.insert('1.0', l)
        objet.config(state=tk.DISABLED)

    else:
        objet.config(state=tk.NORMAL, font="Calibri")
        objet.delete('1.0', tk.END)
        objet.insert('1.0', liste)
        objet.config(state=tk.DISABLED)



# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface_main(tk.Frame):
    def __init__(self, parent):
        """
        Gui principale

        Args:
            parent (tkinter): fenetre principale dans laquelle contenir la GUI
        """
        tk.Frame.__init__(self)
        self.parent = parent

        self.main_display = display.display(self.parent, 0, 0, 20, 8, 10).get_text()
        self.select_player_input = saisie.saisie(self.parent, 0, 1, 20, 10, "nom du joueur")
        self.pendu_play_button = bouton.bouton(self.parent, 1, 1, "jouer", self.pendu_game)


    def pendu_game(self):
        mot = pick_random_word(words_list).upper()
        mot_visible.set_name(mot)
        mot_visible.set_tentative(9)
        mot_cache.set_name("")
        self.hide_word()
        playerName = str(self.select_player_input.get_value()).lower()

        check_player(playerName)

        self.lettre_button = bouton.bouton(self.parent, 2, 1, "valider lettre", self.valider_lettre)
        self.lettre_input = saisie.saisie(self.parent, 2, 2, 2, 1, "lettre")



    def valider_lettre(self):
        l = self.lettre_input.get_value()
        l = str(l).upper()
        lettre.set_name(l)

        str_checked = check_lettre()
        str_score = check_score(joueur.get_name())
        affichage(self.main_display, f"{str_checked} \n {str_score}")

        if mot_visible.get_tentative() == 0:
            self.lettre_button.forget_button()
            self.lettre_input.forget_saisie_label()
            self.lettre_input.forget_saisie()


    def hide_word(self):
        a = hide_word(mot_visible.get_name())
        affichage(self.main_display, a)



# ==================================================================================================
#   SCRIPT
# ==================================================================================================
argument = docopt.docopt(__doc__, version="achetezlejeu")
play = argument.get("<play>")

if play == "play":
    root = tk.Tk()
    menu = menu_bar.class_menu_bar()
    root.title("Jeu du pendu")
    root.config(menu=menu)
    root.geometry("600x200")
    interface_main(root)
    root.mainloop()
else:
    print("Lancez la commande \"python pendu.py play\" afin de jouer.")