from datetime import datetime
from dateutil import relativedelta

def duree(Class):
    frequence = Class.F0

    #on transforme en date
    date_time_obj = datetime.strptime(Class.PDC2, '%Y-%m-%d')
    date_time_obj2 = datetime.strptime(Class.DR1, '%Y-%m-%d')

    #soustraction des 2 dates
    diff = abs(date_time_obj2 - date_time_obj)

    #Calcul à la louche, pour arrondir
    years = diff.days / 365
    months = diff.days / 30
    days = diff.days
    semestriels = diff.days/150
    trimestriels = diff.days / 91

    if (frequence == "jours"):
        result = int(years)
        if (days % 365 >= 182):
            result += 1


    
        first = abs(result)

    frequence = Class.F0

    date_time_obj = datetime.strptime(Class.DCF, '%Y-%m-%d')
    date_time_obj2 = datetime.strptime(Class.DDCI, '%Y-%m-%d')
    diff = date_time_obj2 - date_time_obj
    years = diff.days / 365
    months = diff.days / 30.2
    days = diff.days
    semestriels = diff.days/182
    trimestriels = diff.days / 91

   
    if (frequence == "jours"):
        result = int(years)
        if (years % days >= 182):
            result += 1

    #derniere periode
        second = abs(result)

    #avant derniere periode

    if (Class.F0 == "jours"):
        Class.DUREE = " de " + str(first) + " à " +  str(second) + " ans"   
    #avant derniere date 

        