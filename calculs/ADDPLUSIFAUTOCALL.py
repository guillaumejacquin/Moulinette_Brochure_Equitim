def ADDPLUSIFAUTOCALL(Class):
    if (Class.Typologie == "coupon autocall"):
        Class.ADDPLUSIFAUTOCALL = "+"
    else:
        Class.ADDPLUSIFAUTOCALL = "-"
 
