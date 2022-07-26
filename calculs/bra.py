def bra(Class):
    deg = float(Class.DEG)
    deg = ("{:.2f}".format(deg))
    if (Class.type_bar == "degressif" or Class.type_bar == "  "):
        #Class.BVC = "La barrière de versement du coupon est dégressive au fil du temps. Elle est fixée à <BCPN>% du <NDR> en fin <DU> <F0> 1, puis décroît de <DEG>% chaque <F0> à partir de la fin <DU> <F0> <DDPP> (inclus), pour atteindre <DBAC> du <NDR> à la fin <DU> <F0> <DPRR>."
        Class.BRA = Class.balisedeg2
        Class.BVC = Class.DBAC