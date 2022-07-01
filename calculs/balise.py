import datetime
from dateutil.relativedelta import relativedelta

def balise(Class):
    #les variables
    strike = Class.type_strike
    ndr = Class.NDR
    sjr1 = Class.SJR1
    sjr7 = Class.SJR7
    sjr3 = Class.SJR5
    ddi = Class.DDCI_affichage
    ddi2 = Class.DPCI
    ddi2 = ddi2[8:10] + "/" + ddi2[5:7] + "/" + ddi2[0:4]
    
    #de l' ou du
    if (Class.TDP == "action"):
        du = "de l'"
    else:
        du = "du"


    if (strike == "strike normal"):
        sjr3_tmp = sjr3[:-1]
        mystring = "Le "+ Class.NDR + " correspond au " + sjr3_tmp + " de clôture " + sjr7 + " " + Class.NOMSOUSJACENT +  " le " + ddi

    if (strike == "strike moyen"):
        DCI_split = list(str(Class.DCI).split(", "))
        dci0 = DCI_split[0]
        dci1 = DCI_split[1]
        hebdo = ""
        date_time_obj0 = datetime.datetime.strptime(dci0, '%d-%m-%Y')
        date_time_obj1 = datetime.datetime.strptime(dci1, '%d-%m-%Y')

        date_time_obj1 = date_time_obj1.strftime('%d-%m-%Y')
        tmp = (date_time_obj0 + relativedelta(days=7))                 #je verifie que le premier element et le 2 eme ont bien 7 jours d'écarts pour rajouter le hebdomadaire.
        tmp = tmp.strftime('%d-%m-%Y')
        if (tmp == date_time_obj1):
            hebdo = " hebdomadaire "

        string = "Le" +  Class.NDR + "correspond à la moyenne arithmétique "+ hebdo +" des " + Class.SJR5 + " de clôture aux dates suivantes : " + Class.DCI + "."
        mystring = "Le "+ Class.NDR + " correspond à la moyenne arithmétique "+ hebdo + " des " + sjr3 + " de clôture " + sjr7 + " " + Class.NOMSOUSJACENT + " du " + ddi2 + " au " + ddi

    if (strike == "best strike"):
        mystring = "Le "+ Class.NDR + " correspond au " + sjr3 + " de clôture " + sjr7 + " " + Class.NOMSOUSJACENT + " le plus bas observé aux dates suivantes : \n" + Class.DCI + "."

    Class.balise = mystring


#DCF MAJUSCULE