def bra(Class):
     if (Class.type_bar == "degressif"):
        #Class.BVC = "La barrière de versement du coupon est dégressive au fil du temps. Elle est fixée à <BCPN>% du <NDR> en fin <DU> <F0> 1, puis décroît de <DEG>% chaque <F0> à partir de la fin <DU> <F0> <DDPP> (inclus), pour atteindre <DBAC> du <NDR> à la fin <DU> <F0> <DPRR>."
        Class.BRA = "La barrière de remboursement anticipé automatique est dégressive au fil du temps. Elle est fixée à " + str(Class.BAC)  + " du " + str(Class.NDR) + "en fin de " + str(str(deg).replace(".", ",")) + "% chaque " + Class.F0 + ", pour atteindre , " + str(Class.ABDAC) + "% du "+ str(Class.NDR) + " à la fin du "  + Class.F0 + " " + str(Class.ADPR) +"."
        Class.BVC = "La barrière de versement du coupon est dégressive au fil du temps. Elle est fixée à " + Class.BCPN  + "% du " + Class.NDR
