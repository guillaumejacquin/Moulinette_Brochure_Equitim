def periodederemboursement(Class):
    dr1_tmp = str(Class.DR1)
    dr1_tmp = dr1_tmp[8:10] + "/"+ dr1_tmp[5:7]+ "/" + dr1_tmp[0:4]

    adcf_tmp = str(Class.ADCF)
    adcf_tmp = adcf_tmp[8:10] + "/"+ adcf_tmp[5:7]+ "/" + adcf_tmp[0:4]

    if (Class.F0 == "jours"):
        Class.PERIODE_DE_REMBOURSEMENT = "Chaque jour de bourse, du " + dr1_tmp + " (inclus) jusqu'à la date de constatation finale (exclue)"
        Class.PERIODE_DE_REMBOURSEMENT2 = "Chaque jour de bourse, du " + dr1_tmp + " (inclus) jusqu'à la date de constatation finale (exclue)"