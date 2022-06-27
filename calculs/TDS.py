import datetime
from dateutil.relativedelta import relativedelta

def tds(Class):
    #définition des variables par flemme de les réécrire
    NDR = Class.NDR
    SJR5 = Class.SJR5
    DCI = Class.DCI
    SJR3 = Class.SJR3

    hebdo = ""

    if Class.type_strike == "strike moyen":
        DCI_split = list(DCI.split(", "))
        dci0 = DCI_split[0]
        dci1 = DCI_split[1]
        date_time_obj0 = datetime.datetime.strptime(dci0, '%d-%m-%Y')
        date_time_obj1 = datetime.datetime.strptime(dci1, '%d-%m-%Y')

        date_time_obj1 = date_time_obj1.strftime('%d-%m-%Y')

        tmp = (date_time_obj0 + relativedelta(days=7))                 #je verifie que le premier element et le 2 eme ont bien 7 jours d'écarts pour rajouter le hebdomadaire.
        tmp = tmp.strftime('%d-%m-%Y')

        if (tmp == date_time_obj1):
            hebdo = " hebdomadaire "



        string = "Le" +  NDR + "correspond à la moyenne arithmétique "+ hebdo +" des " + SJR5 + " de clôture aux dates suivantes : " + DCI + "."
        Class.TDS = string

    if Class.type_strike == "best strike":
        string = "Le" +  NDR + "correspond au " + SJR3 + " de clôture aux dates suivantes : " + DCI +"."
        Class.TDS = string

    if Class.type_strike == "strike close" or Class.type_strike == "forward":
        string = "Le" +  NDR + "correspond au"+ SJR3 + " de clôture le " + DCI + "."
        Class.TDS = string
