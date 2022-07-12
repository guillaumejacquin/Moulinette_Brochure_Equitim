def balisedeg(Class):
    deg = float(Class.DEG)
    deg = ("{:.2f}".format(deg))
    if (Class.type_bar == "degressif" or Class.type_bar == "airbag"):
        Class.balisedeg = ", ou si à la date de constatation finale⁽¹⁾, <SJR1> clôture à un <SJR3> supérieur ou égal à <DBAC> de son <NDR>"
        Class.balisedeg2 = "La barrière de remboursement anticipé automatique est dégressive au fil du temps. Elle est fixée à <BAC> du <NDR>  en fin de <F0> <1PR>, puis décroît de " + str(str(deg).replace(".",",")) +"% chaque <F0>, pour atteindre <ABDAC>% du <NDR> à la fin du <F0> <ADPR>."
        Class.balisedeg3 = "<balisedeg2>"

    else:
        Class.balisedeg = ""
        Class.balisedeg2 = ""
        Class.balisedeg3 = "<BAC> DU <NDR> de <SJR1>"

    if ((Class.type_bar == "degressif" or Class.type_bar == "airbag") and Class.DBAC == Class.PDI):
        Class.baliseCM = ""
        Class.deleteblocs.append("Cas médian :")
        Class.deleteblocs.append("(Soit un Taux de Rendement Annuel net de")

    #INCOMPHRENSION#
    if (Class.type_bar == "degressif" or Class.type_bar == "airbag") and Class.DBAC == Class.PDI:
        Class.baliseCM2 = "Le capital n’est donc exposé à un risque de perte à l’échéance\u00281\u0029 que si <SJR1> clôture à un <SJR3> strictement inférieur à <PDI> de son <NDR> à la date de constatation finale⁽¹⁾."
        # Class.deleteblocs.append("Cas médian :")
    else:
        pdi = Class.PDI.replace(".",",")
        Class.baliseCM22 = ("Sinon, si le mécanisme automatique de remboursement anticipé n’a pas été activé au préalable et si, à la date de constatation finale⁽¹⁾, <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> de son <NDR> mais supérieur ou égal à  <PDI> % de ce dernier, l’investisseur récupère l’intégralité de son capital initialement investi. Le capital n’est donc exposé à un risque de perte à l’échéance⁽¹⁾ que si <SJR1> clôture à un <SJR3> strictement inférieur à <PDI> de son <NDR> à la date de constatation finale⁽¹⁾.")
        Class.baliseCM22 = Class.baliseCM22.replace("(1)", '\u00281\u0029')

    #!INCOMPREHENSION!#

    if (Class.type_bar == "degressif" or Class.type_bar == "airbag") and float(Class.DBAC) == float(Class.PDI):
        Class.baliseCM3 = "À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement supérieur à <DBAC> de son <NDR>"
    else:
        Class.baliseCM3 = "À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> mais supérieur ou égal à <PDI> de son <NDR>"

    Class.baliseCM3 = Class.baliseCM3.replace("(1)", '\u00281\u0029')

    if (Class.type_bar == "degressif" or Class.type_bar == "airbag") and float(Class.DBAC) == float(Class.PDI):
        Class.baliseCM4 = """À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement supérieur à <DBAC> de son <NDR> (<NSM> dans cet exemple). L’investisseur récupère alors l’intégralité de son capital initialement investi majorée d’un <GC> de <CPN> par <F0> écoulé depuis le <DDCI> (soit un gain total de <GCE> total)."""

    else: 
        Class.baliseCM4 = """À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> de son <NDR> (<NSM> dans cet exemple). L’investisseur récupère alors l’intégralité de son capital initialement investi.
        """
    Class.baliseCM4 = Class.baliseCM4.replace("(1)", '\u00281\u0029')

    if (Class.type_bar2 == "oui"):
        Class.balisedeg4 = "La barrière de versement du coupon est dégressive au fil du temps. Elle est fixée à <BCPN>% du <NDR> en fin <DU> <F0> 1, puis décroît de <DEG>% chaque <F0> à partir de la fin <DU> <F0> <DDPP> (inclus), pour atteindre <DBAC> du <NDR> à la fin <DU> <F0> <DPRR>."

    if (Class.BFP == Class.PDI):
        Class.baliseCM5 = "À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement supérieur à <PDI> de son <NDR>" 
    else: 
        Class.baliseCM5 = "À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement inférieur à <BFP> mais supérieur ou égal à <PDI> de son <NDR>"



    if (Class.BFP == Class.PDI):
        Class.baliseCM6= "À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement supérieur à <BFP> de son <NDR> (<NSM> dans cet exemple). L’investisseur récupère alors l’intégralité de son capital initialement investi majorée du coupon de <CPN> <Mémoire6>."
    else:
       Class.baliseCM6 = "À la date de constatation finale\u00281\u0029, <SJR1> clôture à un <SJR3> strictement inférieur à <BFP> de son <NDR> (<NSM> dans cet exemple) mais strictement supérieur à <PDI> de son <NDR>. L’investisseur récupère alors l’intégralité de son capital initialement investi."
    

    