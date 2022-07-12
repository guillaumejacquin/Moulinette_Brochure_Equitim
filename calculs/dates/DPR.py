def DPR(Class):
    #date de premeir remborusement
    dpr = Class.DPR
    annee = dpr[0:4]
    mois = dpr[5:7]
    jours = dpr[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DPR_affichage = mystring