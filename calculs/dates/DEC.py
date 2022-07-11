def dec(Class):
    dec = Class.DEC
    annee = dec[0:4]
    mois = dec[5:7]
    jours = dec[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DEC_affichage = mystring
    #date d'echeance, affichage 
    DADR_affichage(Class)

def DADR_affichage(Class):
    dadr = Class.DADR
    annee = dadr[0:4]
    mois = dadr[5:7]
    jours = dadr[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DADR_affichage = mystring
    #date d'echeance, affichage 