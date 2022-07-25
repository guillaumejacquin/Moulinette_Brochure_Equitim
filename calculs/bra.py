def bra(Class):
    deg = float(Class.DEG)
    deg = ("{:.2f}".format(deg))
    if (Class.type_bar == "degressif" or Class.type_bar == "  "):
        #Class.BVC = "La barrière de versement du coupon est dégressive au fil du temps. Elle est fixée à <BCPN>% du <NDR> en fin <DU> <F0> 1, puis décroît de <DEG>% chaque <F0> à partir de la fin <DU> <F0> <DDPP> (inclus), pour atteindre <DBAC> du <NDR> à la fin <DU> <F0> <DPRR>."
        Class.BRA = "La barrière de remboursement anticipé automatique est dégressive au fil du temps. Elle est fixée à <BAC> du <NDR>  en fin de <F0> <1PR>, puis décroît de " + str(str(deg).replace(".",",")) +"% chaque <F0>, pour atteindre <ABDAC>% du <NDR> à la fin du <F0> <ADPR>."
        Class.BVC = "La barrière de versement du coupon est dégressive au fil du temps. Elle est fixée à " + Class.BCPN  + "% du " + Class.NDR