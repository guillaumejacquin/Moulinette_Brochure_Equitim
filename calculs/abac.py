def abac(Class):
    if (Class.type_bar == "" or Class.type_bar == "degressif"):
        Class.ABAC = "la barrière dégressive de remboursement anticipé automatique⁽¹⁾"
    else:
        mystring = str(Class.BAC) + "% de son <NDR>"
        Class.ABAC = mystring

def abac2(Class):
    if Class.type_bar2 == "oui" and Class.BCPN_is_degressif == "oui":
        Class.ABAC2 = "la barrière dégressive de versement du coupon"

    else:
        Class.ABAC2 = "la barrière dégressive de remboursement automatique⁽¹⁾"