
from turtle import fillcolor
import plotly.express as px
import kaleido

green = "#00B050"
blue = "#002E8A"
red = "#C00000"
black = "#000000"

def params(fig):
    fig.update_xaxes(range=[0.5,90])
    fig.update_yaxes(range=[27.75,175])
    # fig.update_yaxes(ticks="outside", tickwidth=1, tickcolor='crimson', ticklen=10, col=1)

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0],
                    ticktext= ["","", "", ""],
                    ),

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [20, 30,40, 50, 60,70,80,90,100,110,120,130, 140, 150],
                    ticktext= ["20%", "30%", "40%", "50%", "60%","70%","80%", "90%", "100%", "110%", "120%", "130%", "140%", "150%"],
                    color="black"
                    ),
                    
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0.5],
                    ticktext= ["<b>Lancement</b>"],
                    ),
    fig.update_layout(
        legend=dict(
            itemclick="toggleothers",
            itemdoubleclick="toggle"),
            autosize=True,

            plot_bgcolor='rgb(255,255,255)',
            margin=dict(
                l=50,
                r=0,
                b=20,
                t=50,
                pad=0),
            paper_bgcolor='white')
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        }) 
    return(fig)


def axes_ordonees(fig):
    fig.add_annotation( x=1.5, y=160, ax=1.5, ay=28, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')


    fig.add_annotation(x=82, y=28, ax=1, ay=28, xref='x', yref='y', axref='x', ayref='y', text='',
    showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

    return(fig)

def traces(Class, fig):
    niveau_de_référence = float(Class.BAC)
    avant_dernier_niveau_de_reference = float(Class.ABDAC)
    derniere_observation = float(Class.DBAC)
    perte_capital = float(Class.PDI)
    niveau_de_scénario_déf = float(Class.NSD)
    premier_niveau_autocall = float(Class.BAC)
    x_scenario_def = 0
    #-----------------------Mettre en int si 100.0 par ex mais pas si 50.2"
    x_niveau_ref = 0
    x_derniere_observation = 0
    x_perte_capital = 0
    x_niveau_def = 0

    text_legende = Class.SJR3.capitalize() + "<br>"+ Class.SJR7 +  " par <br>rapport à son <br>" + Class.NDR
    
    fig.add_annotation(x=2.2, y=172, text= (text_legende), showarrow=False,
                    font=dict(family="Proxima Nova", size=10, color=black ), align="left")

    if (niveau_de_référence).is_integer():
        niveau_de_référence = int(niveau_de_référence)
        x_niveau_ref = 0.5


    if (derniere_observation).is_integer():
        derniere_observation = int(derniere_observation)
        x_derniere_observation = 0.5

    if (perte_capital).is_integer():
        perte_capital = int(perte_capital)
        x_perte_capital = 0.5

    if (niveau_de_scénario_déf).is_integer():
        niveau_de_scénario_déf = int(niveau_de_scénario_déf)
        x_scenario_def = 0.5
    #-----------------------Mettre en int si 100.0 par ex mais pas si 50.2"

    x_vertical_line = 81 #le x de la ligne verticale pour aligner les elements
    pasdedegressivite = float(Class.DEG)
    #la ligne verticale a droite noire
    fig.add_shape(type="line",
    x0=x_vertical_line, y0=140, x1=x_vertical_line, y1=18,
    line=dict(color=black, width=2),  line_dash="dot")

    #la ligne horizontale = niveau de référence verte

    # fig.add_shape(type="line",
    # x0=30, y0=premier_niveau_autocall, x1=61, y1=avant_dernier_niveau_de_reference + 2 * pasdedegressivite,
    # line=dict(color=green, width=3),  line_dash="dash")

    add_remontee_var = 0    
    if Class.type_bar == "degressif" or Class.type_bar == "  ":
        add_remontee_var = 1
    # fig.add_shape(type="line",
    # x0=69, y0=avant_dernier_niveau_de_reference + add_remontee_var, x1=73, y1=avant_dernier_niveau_de_reference + add_remontee_var,
    # line=dict(color=green, width=3),  line_dash="dash")


    if float(Class.DBAC) >= niveau_de_référence:
        fig.add_annotation(x=x_vertical_line +4.75 - x_niveau_ref, y=niveau_de_référence,text= (str(niveau_de_référence) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color=green ), align="left")

        fig.add_shape(type="line",
        x0=x_vertical_line, y0=niveau_de_référence, x1= x_vertical_line - 3, y1=niveau_de_référence,
        line=dict(color=green, width=4))
    else:
        fig.add_annotation(x=x_vertical_line +4.75 - x_niveau_ref, y=niveau_de_référence,text= (str(niveau_de_référence) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color=black ), align="left")

        fig.add_shape(type="line",
        x0=x_vertical_line, y0=niveau_de_référence, x1= x_vertical_line - 3, y1=niveau_de_référence,
        line=dict(color=black, width=4))
    
    fig.add_annotation(x=x_vertical_line +4.75 - x_derniere_observation, y=derniere_observation,text= (str(derniere_observation) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color=blue ), align="left")
    
    fig.add_shape(type="line",
    x0=x_vertical_line, y0=derniere_observation, x1= x_vertical_line - 3, y1=derniere_observation,
    line=dict(color=blue, width=4))

    fig.add_annotation(x=x_vertical_line +4.75 - x_perte_capital, y=perte_capital,text= (str(perte_capital) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color=red ), align="left")

    fig.add_shape(type="line",
    x0=x_vertical_line, y0=perte_capital, x1= x_vertical_line - 3, y1=perte_capital,
    line=dict(color=red, width=4))
   
    if (float(avant_dernier_niveau_de_reference) < premier_niveau_autocall):
            fig.add_annotation(x=70, y=avant_dernier_niveau_de_reference + 2 * pasdedegressivite + add_remontee_var + 8 ,text= str(avant_dernier_niveau_de_reference) +"%", showarrow=False,
            font=dict(family="Proxima Nova", size=14, color=green), align="left")
   
    # fig.add_annotation(x=x_vertical_line + 4.75 - x_scenario_def, y=niveau_de_scénario_déf,text= (str(niveau_de_scénario_déf) + "%" ), showarrow=False,
    #                 font=dict(family="Proxima Nova", size=15, color=blue ), align="left")
    
    # fig.add_shape(type="line",
    # x0=x_vertical_line, y0=niveau_de_scénario_déf, x1= x_vertical_line - 3, y1=niveau_de_scénario_déf,
    # line=dict(color=blue, width=4))

    # fig.add_shape(type="line",
    # x0=x_vertical_line, y0=niveau_de_scénario_déf, x1= x_vertical_line - 3.5, y1=niveau_de_scénario_déf,
    # line=dict(color=blue, width=6))
    derniere_observation = float(Class.DBAC)
    if (derniere_observation).is_integer():
        derniere_observation = int(derniere_observation)
        x_derniere_observation = 0.5
    if (Class.Typologie == "coupon autocall"):

        fig.add_annotation(x=x_vertical_line + 4.75 - x_niveau_ref, y=Class.DBAC,text= (str(derniere_observation) + "%" ), showarrow=False,
            font=dict(family="Proxima Nova", size=15, color=green ), align="left")
        fig.add_shape(type="line",
            x0=x_vertical_line, y0=derniere_observation, x1= x_vertical_line - 3, y1=derniere_observation,
            line=dict(color=green, width=4))
                
    if (float(niveau_de_référence) == float(Class.DBAC)):
        fig.add_annotation(x=x_vertical_line + 4.75 - x_niveau_ref, y=Class.DBAC,text= (str(Class.DBAC) + "%" ), showarrow=False,
            font=dict(family="Proxima Nova", size=15, color=green ), align="left")
        fig.add_shape(type="line",
            x0=x_vertical_line, y0=Class.DBAC, x1= x_vertical_line - 3, y1=Class.DBAC,
            line=dict(color=green, width=4))

    if float(Class.DBAC) != float(Class.BAC):
            fig.add_annotation(x=x_vertical_line +4.75 - x_derniere_observation, y=derniere_observation,text= (str(derniere_observation) + "%" ), showarrow=False,
                font=dict(family="Proxima Nova", size=15, color=green ), align="left")
        
            fig.add_shape(type="line",
            x0=x_vertical_line, y0=derniere_observation, x1= x_vertical_line - 3, y1=derniere_observation,
            line=dict(color=green, width=4))

def texte(Class, fig):
    indice = Class.Nom


    fig.add_annotation(x=39, y=175 ,text= ("<b>Evolution "  + Class.SJR7 + "</b>" ), showarrow=False,
                        font=dict(family="Proxima Nova", size=20, color=black ), align="left")

    pasdedegressivite = float(Class.DEG)
    if pasdedegressivite == 0:
        degressive = ""
    else:
        degressive = "dégressivité"

    if (Class.Typologie == "coupon autocall"):
        text = "Seuil d'activation du mécanisme "  + degressive +" de remboursement anticipé automatique <br> à partir de la fin du " + str(Class.F0)+ " " + str(int(Class.PR1)) +  " jusqu'à la fin du "+ str(Class.F0)+ " " + str(Class.ADPR) + " et de versement des gains à l'échéance"
        x_a = 44.5

    else:
        text = "Seuil d'activation du mécanisme  "  + degressive +" de remboursement anticipé automatique <br> à partir de la fin du " + str(Class.F0)+ " " + str(int(Class.PR1)) +  " jusqu'à la fin du "+ str(Class.F0)+ " " + str(Class.ADPR)
        x_a = 44.5
        
    if (Class.F0 == "jours"):
        text = "Seuil d'activation du mécanisme "  + degressive +" de remboursement anticipé automatique <br> à partir " + Class.PERIODE_DE_REMBOURSEMENT
        x_a = 44.5
    fig.add_annotation(x=x_a, y=153+8 ,text= text, showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")

   
    fig.add_annotation(x=24.5, y=138 + 8 ,text= ("Part de capital remboursé" ), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")         

    fig.add_annotation(x=28, y=144.5 +8  ,text= ("Seuil de perte en capital à l'échéance" ), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")

    fig.add_shape(type="line",
        x0=7, y0=153 +8 , x1=12, y1=153 + 8,
        line=dict(color=green, width=2), line_dash="dot")    

        
    fig.add_annotation(x=27.5, y=130 + 8 ,text= ("Simulation de l'évolution de l'" + Class.SJR1 ), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")
    
    fig.add_shape(type="line",
        x0=7, y0=130 + 8, x1=12, y1=130 + 8,
        line=dict(color="#D9CD9F", width=2))    

    fig.add_annotation(x=42.5, y=124 + 8 ,text= ("Différence entre le montant de remboursement du produit et le niveau du sous-jacent" ), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")

    fig.add_shape(type="line",
        x0=7, y0=124 + 8, x1=12, y1=124 + 8,
        line=dict(color="orange", width=1), line_dash="dot")                   
    
    if (Class.Typologie == "coupon phoenix"):
        fig.add_annotation(x=26, y=113 + 8 ,text= ("Coupon " + Class.F1 + " de " + str(str(Class.CPN).replace(".", ",")) +"%"), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")


    fig.add_shape(type="line",
        x0=7, y0=144 +8, x1=12, y1=144 + 8,
        line=dict(color=red, width=2))
        
    fig.add_shape(type="circle",
        xref="x", yref="y",
        fillcolor=blue,
        x0=9.5 - 0.95 , y0= 137 - 1.5 + 8 , x1=9.5 + 0.95, y1 = 138 + 1.5 + 8,
        line_color=blue,
)    

    return(fig)

def athena_annotations(Class, fig):
    last = Class.DPRR
    first = 1 
    prappel = Class.PR1
    frequence = Class.F0
    prefix = ""

    premier_niveau_autocall = float(Class.BAC)
    avant_dernier_niveau_de_reference = float(Class.ABDAC)
    pasdedegressivite = float(Class.DEG)

 
    if frequence == "jours" or frequence == "année":
        prefix = "A"
    
    if frequence == "mois":
        prefix = "M"
    
    if frequence == "trimestre":
        prefix = "T"
    
    if frequence == "semestre":
        prefix = "S"

    prappel = int(Class.PR1)
    cpn = float(Class.CPN)

    #pour coupon phoenix, +prappel = 1
    # fig.add_shape(type="circle",
    # xref="x", yref="y",
    # fillcolor=blue,
    # x0=20 - 0.95 , y0= perfmax -1.705, x1=20 + 0.95, y1 = perfmax + 1.705,
    # line_color=blue,
    # )

    fig.add_shape(type="line",
            x0=20, y0=premier_niveau_autocall, x1=22.5 , y1=premier_niveau_autocall ,
            line=dict(color=green, width=3))
    
        
    fig.add_shape(type="line",
                    x0=23, y0=premier_niveau_autocall, x1=70, y1=float(Class.ABDAC),
                    line=dict(color=green, width=3),  line_dash="dash")
    if (Class.type_bar != "airbag"):
        fig.add_shape(type="line",
                        x0=70, y0=float(Class.ABDAC), x1=80.5, y1=float(Class.DBAC),
                        line=dict(color=green, width=3),  line_dash="dash")

                    
    if (Class.F0 != "année"):
        fig.update_xaxes(tickangle=0,
                        tickmode = 'array',
                        tickvals = [1.5, 10, 15,  20, 40.5, 61, 71, 81],
                        ticktext= ["<b>Lancement</b>", prefix + str(int(first)), "...", prefix + str(int(prappel)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                        color="black"
                        ),
    else:
        if (int(prappel) == 2):
            fig.update_xaxes(tickangle=0,
                            tickmode = 'array',
                            tickvals = [1.5, 10,  20, 40.5, 61, 71, 81],
                            ticktext= ["<b>Lancement</b>", prefix + str(int(first)), prefix + str(int(prappel)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                            color="black"
                            ),
        elif (int(prappel) == 1):
            fig.update_xaxes(tickangle=0,
                            tickmode = 'array',
                            tickvals = [1.5, 10, 40.5, 61, 71, 81],
                            ticktext= ["<b>Lancement</b>", prefix + str(int(first)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                            color="black"
                            ),
        else:
              fig.update_xaxes(tickangle=0,
                        tickmode = 'array',
                        tickvals = [1.5, 10, 15,  20, 40.5, 61, 71, 81],
                        ticktext= ["<b>Lancement</b>", prefix + str(int(first)), "...", prefix + str(int(prappel)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                        color="black"
                        ),
    if (Class.F0 == "jours"):
        dcf_tmp = str(Class.DCF)
        dcf_tmp = dcf_tmp[8:10] + "/"+ dcf_tmp[5:7]+ "/" + dcf_tmp[0:4]

        dr1_tmp = str(Class.DPR)
        dr1_tmp = dr1_tmp[8:10] + "/"+ dr1_tmp[5:7]+ "/" + dr1_tmp[0:4]
        fig.update_xaxes(tickangle=0,
                        tickmode = 'array',
                        tickvals = [1.5, 20, 40.5, 81],
                        ticktext= ["<b>Lancement</b>", dr1_tmp, "....",  dcf_tmp],
                        color="black"
                        ),
 # fig.add_shape(type="line",
    # x0=76, y0=avant_dernier_niveau_de_reference, x1=79, y1=avant_dernier_niveau_de_reference,
    # line=dict(color=green, width=3),  line_dash="dash")

    fig.update_xaxes(ticks="outside", col=1)


def phoenix_annotations(Class, fig):
    print("Phoenix")
    coupon = float(Class.BCPN)
    derniere_observation = float(Class.DBAC)
    x_vertical_line = 81
    last = Class.DPRR
    first = 1 
    prappel = Class.PR1
    p2 = 2
    avant_dernier_niveau_de_reference = float(Class.ABDAC)
    pasdedegressivite = float(Class.DEG)
    premier_niveau_autocall = float(Class.BAC)

    frequence = Class.F0
    prefix = ""
    prappel = float(Class.PR1)
    cpn = float(Class.CPN)
    perfmax = 100 + prappel * cpn
    
    if frequence == "jours" or frequence == "année":
        prefix = "A"
    
    if frequence == "mois":
        prefix = "M"
    
    if frequence == "trimestre":
        prefix = "T"
    
    if frequence == "semestre":
        prefix = "S"


    #legende
    fig.add_annotation(x=27, y=133 -8 ,text= ("Seuil de versement des coupons" ), showarrow=False,
    font=dict(family="Proxima Nova", size=10, color=black), align="left")         
    fig.add_shape(type="line",
        x0=7, y0=133 - 8, x1=12, y1=133 - 8,
        line=dict(color=blue, width=1), line_dash="dot")    
    #legende

    if (coupon != derniere_observation):
            fig.add_annotation(x=x_vertical_line +4.75, y=coupon,text= (str(coupon) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color=blue ), align="left")
 
    if (p2 == prappel):
        fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [1.5, 10, 20, 41,  61, 71, 81],
                    ticktext= ["<b>Lancement</b>", prefix + str(int(first)), prefix + str(int(p2)), "......." , prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                       color="black"
                 ),  
        start_green_line = 20
        


    else:
        fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [1.5, 10, 15, 22.5, 30, 45, 61, 71, 81],
                    ticktext= ["<b>Lancement</b>", prefix + str(int(first)), str(prefix) + str(p2), ".....", prefix + str(int(prappel)),".......",  prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                    color="black"
               ),
               
        start_green_line = 30
    
 
        tmp = avant_dernier_niveau_de_reference + 2 * pasdedegressivite
        compteur = 0
        if tmp < coupon and pasdedegressivite > 0: 
            while  tmp <= coupon :
                tmp += pasdedegressivite
                compteur +=1



            start_white_line = (71 - compteur * 3.5)
            
            # fig.add_shape(type="line",
            # x0=start_white_line, y0=coupon, x1=81, y1=coupon,
        # line=dict(color="white", width=2, fillcolor="white"))


            fig.add_shape(type="line",
            x0=start_green_line + 3 , y0=premier_niveau_autocall, x1=60 , y1=coupon + 0.5 ,
            line=dict(color=green, width=3),  line_dash="dash")

        else:
            fig.add_shape(type="line",
            x0=start_green_line - 1.5 , y0=premier_niveau_autocall, x1=start_green_line + 2 , y1=premier_niveau_autocall ,
            line=dict(color=green, width=3))


            fig.add_shape(type="line",
                            x0=start_green_line, y0=premier_niveau_autocall, x1=70, y1=float(Class.ABDAC),
                            line=dict(color=green, width=3),  line_dash="dash")

            if (Class.type_bar != "airbag"):
                fig.add_shape(type="line",
                                x0=70, y0=float(Class.ABDAC), x1=80.5, y1=float(Class.DBAC),
                                line=dict(color=green, width=3),  line_dash="dash")

    fig.add_shape(type="line",
            x0=start_green_line - 1.5 , y0=premier_niveau_autocall, x1=start_green_line + 2 , y1=premier_niveau_autocall ,
            line=dict(color=green, width=3))        

    fig.add_shape(type="line",
            x0=2 , y0=float(Class.BCPN), x1=78 + 2 , y1=float(Class.BCPN) ,
            line=dict(color=blue, width=3), line_dash="dash")
              
    if (Class.F0 != "année"):
            fig.update_xaxes(tickangle=0,
                            tickmode = 'array',
                            tickvals = [1.5, 10, 15,  20, 40.5, 61, 71, 81],
                            ticktext= ["<b>Lancement</b>", prefix + str(int(first)), "...", prefix + str(int(prappel)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                            color="black"
                            ),
    else:
            if (int(prappel) == 2):
                fig.update_xaxes(tickangle=0,
                                tickmode = 'array',
                                tickvals = [1.5, 10,  20, 40.5, 61, 71, 81],
                                ticktext= ["<b>Lancement</b>", prefix + str(int(first)), prefix + str(int(prappel)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                                color="black"
                                ),
            elif (int(prappel) == 1):
                fig.update_xaxes(tickangle=0,
                                tickmode = 'array',
                                tickvals = [1.5, 10, 40.5, 61, 71, 81],
                                ticktext= ["<b>Lancement</b>", prefix + str(int(first)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                                color="black"
                                ),
            else:
                fig.update_xaxes(tickangle=0,
                            tickmode = 'array',
                            tickvals = [1.5, 10, 15,  20, 40.5, 61, 71, 81],
                            ticktext= ["<b>Lancement</b>", prefix + str(int(first)), "...", prefix + str(int(prappel)), "....", prefix + str(last - 2), prefix + str(last - 1), prefix + str(last)],
                            color="black"
                            ),
    fig.update_xaxes(ticks="outside", col=1)

def is_athena_or_phoenix_annotations(Class, fig):
    typologie = Class.Typologie #coupon phoenix
    prappel = Class.PR1
    cpn = float(Class.CPN)

    if typologie == "coupon autocall":
        athena_annotations(Class, fig)

    else:
        phoenix_annotations(Class, fig)

    if typologie == "coupon autocall":

        perfmax = 100 + prappel * cpn
        perfmax = (f'{float(perfmax):.2f}')
        string = str(perfmax)  +"% ="
        string = string.replace(".", ",")
        Class.R1 = string[:-2]

        cpn = float(Class.CPN)
        len_cpn = (str(cpn)[::-1].find('.'))

        if (len_cpn < 2):
                cpn = (f'{float(Class.CPN):.2f}')        
        str2 = "100% + " + str(int(prappel)) + " x " + str(cpn) + "%" 
        
        str2 = str2.replace(".", ",")
        Class.r1 = str2

    else:
        perfmax = 100 + 1 * cpn

        len_cpn = (str(perfmax)[::-1].find('.'))

        if (len_cpn < 2):
            perfmax = (f'{float(perfmax):.2f}')


        cpn = (f'{float(cpn):.2f}')
        cpn = float(Class.CPN)
        len_cpn = (str(cpn)[::-1].find('.'))

        if (len_cpn < 2):
                cpn = (f'{float(Class.CPN):.2f}')

        string = str(perfmax)  + "% ="
        str2 ="100% + 1 x " + str(cpn) + "%"
        Class.r1 = str2

    fig.add_annotation(x=30, y=110 ,text= (string ), showarrow=False,
                        font=dict(family="Proxima Nova", size=16, color=blue), align="left")

    fig.add_annotation(x=44.5, y=110 ,text=(str2), showarrow=False,
                        font=dict(family="Proxima Nova", size=16, color="#D5C691" ), align="left")

def smallgraph3(Class, name):
    fig = px.line()
    params(fig)
    axes_ordonees(fig)
    traces(Class, fig)
    texte(Class, fig)

    is_athena_or_phoenix_annotations(Class, fig)
    

    #fig.show()
    fig.write_image(name, format="png", scale=2, engine='kaleido')


