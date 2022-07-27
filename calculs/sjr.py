def SJR(Class):
    sousjacent = Class.sous_jacent

    #Réalisation des  phrases
    if sousjacent == "mono action":
        Class.SJR1 = "l’action"
        Class.SJR2 = "celle-ci"
        Class.SJR3 = "cours"
        Class.SJR4 = "de"
        Class.SJR5 = "cours"
        Class.SJR6 = "de l'action"
        Class.SJR7 = "de l'action"
        Class.SJR8 = "L'action"


    if sousjacent == "wo action":
        Class.SJR1 = "l’action la moins performante"
        Class.SJR2 = "celle-ci"
        Class.SJR3 = "cours"
        Class.SJR4 = "de"
        Class.SJR5 = "cours"
        Class.SJR6 = "des actions"
        Class.SJR7 = "de l'action la moins performante"
        Class.SJR8 = "Les actions"



    if sousjacent == "equipondéré action":
        Class.SJR1 = "le panier équipondéré"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "du"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "des actions"
        Class.SJR7 = "du panier équipondéré"
        Class.SJR8 = "Les actions"


    if sousjacent == "mono indice":
        Class.SJR1 = "l'indice"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "de " + str(Class.SJR1)
        Class.SJR7 = "de l'indice"
        Class.SJR8 = "L'indice"


    if sousjacent == "wo indice":
        Class.SJR1 = "l'indice le moins performant"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "des indices"
        Class.SJR7 = "de l'indice le moins performant"
        Class.SJR8 = "Les indices"

    if sousjacent == "equipondéré indice":
        Class.SJR1 = "le panier équipondéré"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "des indices"
        Class.SJR7 = "du panier équipondéré"
        Class.SJR8 = "Les indices"

    Class.SJR1M = Class.SJR1.capitalize()
    Class.SJR2M = Class.SJR2.capitalize()
    Class.SJR3M = Class.SJR3.capitalize()
    Class.SJR4M = Class.SJR4.capitalize()
    Class.SJR5M = Class.SJR5.capitalize()
    Class.SJR6M = Class.SJR6.capitalize()
    Class.SJR7M = Class.SJR7.capitalize()
    Class.SJR8M = Class.SJR8.capitalize()

#equipondere action ou equipondéré indice



#best strike ou strike moyen, niveau de référence ou cours de rèf 
#si panier equipondéré: