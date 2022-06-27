
from turtle import fillcolor
import plotly.express as px
import kaleido

green = "#00B050"
blue = "#002E8A"
red = "#C00000"
black = "#000000"

def params(fig):
    fig.update_xaxes(range=[0.5,90])
    fig.update_yaxes(range=[100,145])
  

  
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [],
                    ticktext= [],
                    ),

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [],
                    ticktext= [],
                       color="black"
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



def traces(Class, fig):

    add_remontee_var = 0    
    if Class.type_bar == "degressif":
        add_remontee_var = 1

def texte(Class, fig):
    indice = Class.Nom


    fig.add_annotation(x=39, y=145 ,text= ("<b>Evolution "  + Class.SJR7 + "</b>" ), showarrow=False,
                        font=dict(family="Proxima Nova", size=20, color=black ), align="left")
    pasdedegressivite = float(Class.DEG)
    if pasdedegressivite == 0:
        degressive = ""
    else:
        degressive = "dégressivité"

    if (Class.Typologie == "coupon autocall"):
        text = "Seuil d'activation du mécanisme de la barrière "  + degressive +" de remboursement anticipé automatique <br> à partir de la fin du " + str(Class.F0)+ " " + str(Class.PR1) +  " jusqu'à la fin du "+ str(Class.F0)+ " " + str(Class.ADPR) + " et de versement des gains à l'échéance"
        x_a = 46.5
    else:
        text = "Seuil d'activation du mécanisme de la barrière "  + degressive +" de remboursement anticipé automatique <br> à partir de la fin du " + str(Class.F0)+ " " + str(Class.PR1) +  " jusqu'à la fin du "+ str(Class.F0)+ " " + str(Class.ADPR)
        x_a = 43.4
    fig.add_annotation(x=x_a, y=133 + 8 ,text= (text), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")

    fig.add_annotation(x=28, y=124.5 + 8 ,text= ("Seuil de perte en capital à l'échéance" ), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")
   
    fig.add_annotation(x=24.5, y=118 + 8 ,text= ("Part de capital remboursé" ), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")      

    #----------------------------------------#
    # fig.add_annotation(x=42.5, y=110 + 8 ,text= ("Différence entre le montant de remboursement du produit et le niveau du sous-jacent" ), showarrow=False,
    #                     font=dict(family="Proxima Nova", size=10, color=black ), align="left")

    # fig.add_shape(type="line",
    #     x0=7, y0=110 + 8, x1=12, y1=110 + 8,
    #     line=dict(color="orange", width=1), line_dash="dot")    
    #----------------------------------------#

    fig.add_annotation(x=27.5, y=110 + 8 ,text= ("Simulation de l'évolution de l'" + Class.SJR1 ), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")
    
    fig.add_shape(type="line",
        x0=7, y0=110 + 8, x1=12, y1=110 + 8,
        line=dict(color="#D9CD9F", width=2))    

                        
    if (Class.Typologie == "coupon phoenix"):
        fig.add_annotation(x=26, y=99 + 8 ,text= ("Coupon " + Class.F1 + " de " + str(str(Class.CPN).replace(".", ",")) +"%"), showarrow=False,
                        font=dict(family="Proxima Nova", size=10, color=black ), align="left")


    fig.add_shape(type="line",
        x0=7, y0=133 + 8, x1=12, y1=133 + 8,
        line=dict(color=green, width=2), line_dash="dot")    

        

    fig.add_shape(type="line",
        x0=7, y0=124 + 8, x1=12, y1=124 + 8,
        line=dict(color=red, width=2))
        
    fig.add_shape(type="circle",
        xref="x", yref="y",
        fillcolor=blue,
        x0=9.5 - 2 , y0= 117 - 0.75 + 8 , x1=9.5 + 2, y1 = 118 + 0.75 + 8,
        line_color=blue,
)    
    return(fig)


def header(Class, name):
    fig = px.line()
    params(fig)
    texte(Class, fig)

    #fig.show()
    fig.write_image(name, format="png", scale=2, engine='kaleido')

