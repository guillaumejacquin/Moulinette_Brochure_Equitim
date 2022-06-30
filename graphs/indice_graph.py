from ast import Pass, Return
from asyncio import exceptions
from tkinter import EXCEPTION, font
from unittest import registerResult
from matplotlib import ticker
from pandas_datareader import data
import pandas as pd
import plotly.express as px
from pandas.tseries.offsets import Day, BDay
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

def get_value_array(yearstoadd, start_date , df, tickers):
    bdays=BDay()
    start = start_date - relativedelta(years=yearstoadd)
    start = start.strftime('%Y-%m-%d')
    mask = (df[tickers[0]] >= start) # JOUR SUIVANT

    result = df[mask]["Unnamed: 1"].iloc[0]
    result = df["Unnamed: 1"].iloc[-1] / result -1
    result = result * 100

    return result
    
def indice_simple_tickers(tickers, Class, Name):
    bdays=BDay()
    df = pd.read_excel (r'database/database_indice.xlsx', sheet_name=tickers[0])
    df = df.iloc[1: , :]

    fig = px.line(data_frame = df[tickers[0]]
                        ,x = df[tickers[0]]
                        ,y = [df["Unnamed: 1"]],
                        title="Points",
                        )

    fig.update_traces(line_color='#B9A049')

    fig.update_layout(
            xaxis=dict(
                showline=False,
                showgrid=False,
                title="",
                ticks='inside',
                
                visible= True,
                showticklabels = True,
                tickfont=dict(
                    family='Proxima Nova',
                    size=12,
                    color='rgb(82, 82, 82)',
                    
                    )
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=False,
                showticklabels=True,
                ticks='inside',
                gridwidth=1,
                gridcolor='rgb(242, 242, 242)',
                linecolor='rgb(0, 0, 0)',
                linewidth= 1,
                title=None, 
                tickfont=dict(
                    family='Proxima Nova',
                    size=12,
                    color='rgb(82, 82, 82)',
                    
                    )
            ),#E5EBF7  
                title=dict(
        x = 0.1,
        y=0.85,
        font=dict(
        family="Proxima Nova",
            size=14,
        )
        ),
            showlegend = False,
            plot_bgcolor='white',
        )

    fig.layout.xaxis.color = 'black'
    fig.layout.yaxis.color = 'black'

    fig.data[0].line.color = 'rgb(197, 175, 92)'
    fig.data[0].line.width = 1
    first_date= df[tickers[0]].iloc[0]
    last_date = df[tickers[0]].iloc[-1]
    max_value = df["Unnamed: 1"].max() + 2/100 * df["Unnamed: 1"].max()

    
    fig.add_annotation(x=last_date + relativedelta(months=6), y=-20, ax=first_date - relativedelta(days=30), ay=-20, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=False, arrowhead=3, arrowwidth=1, arrowcolor='white')

    fig.add_annotation(x=first_date - relativedelta(days=50), y=max_value + max_value/5, ax=first_date - relativedelta(days=50) , ay=-20, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=False, arrowhead=3, arrowwidth=1, arrowcolor='white')


    fig.add_annotation(x=last_date + relativedelta(months=6), y=25, ax=first_date - relativedelta(days=40), ay=25, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')
    
    fig.add_annotation(x=first_date - relativedelta(days=15), y=max_value + max_value/5, ax=first_date - relativedelta(days=15) , ay=10, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')

    time_to_add_style = relativedelta(days=5)    
    time_to_add = relativedelta(years=1)    
    
    lastdate = last_date
    lastdate_tmp =  last_date - time_to_add_style
    firstdate = first_date
    firstdate_tmp = firstdate
    seconddate = firstdate + 2 * time_to_add
    thirddate = firstdate + 2 * 2 * time_to_add
    fourthdate = firstdate + 3 *2 * time_to_add
    fivthdate = firstdate + 4 * 2 * time_to_add
    sixthdate = firstdate + 5 *2 * time_to_add 
    month = str(firstdate)[5:7]
    day = str(firstdate)[8:10]
    year = str(firstdate)[0:4]
    monthfin = str(lastdate)[5:7]
    dayfin = str(lastdate)[8:10]
    yearfin = str(lastdate)[0:4]        # ###############LE STYLE D AFFICHAGE###########
    
    firstdate_visu = str(day) + "/" + str(month) + "/" + str(year) 
    seconddate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2)
    thirddate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 2)
    fourthdate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 3)
    fivthdate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 4)
    sixthdate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 5 )
    lastdate_value = str(dayfin) + "/" + str(monthfin) + "/" + str(yearfin) 
    ###############LE STYLE D AFFICHAGE###########
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [firstdate_tmp, seconddate, thirddate, fourthdate, fivthdate, sixthdate, lastdate],
                    ticktext= [firstdate_visu, seconddate_visu, thirddate_visu, fourthdate_visu, fivthdate_visu, sixthdate_visu, lastdate_value]
                    ),
    fig.write_image(Name, format="png", scale=4, engine='kaleido')


    simple_yahoo_value_arrays = [1, 3 ,5 , 10, 12 ] # le tableau pour la boucle pour les années
    for i in Class.Yahoo:
        my_array = [] #j'initie un nouveau tableau a chaque sousjacent

        for i in simple_yahoo_value_arrays: #je fias une boucle pour parcourir les valeurs (1, 3,5 etc)
            pass
            try:
                result = get_value_array(int(i), last_date, df, tickers)
                result = ("{:.2f}".format(result))
                result = result.replace(".", ",") #joli format écrit
                result = result + "%"

                my_array.append(result)
            except Exception:
                my_array.append("N/A")
                print("Le tableau des perfs pour mono indice a fail ici")
                pass
            Class.Yahoo_value.append(my_array)
        # print(last_date, ",k,,,,,,,,,,,,,,,,,,,,,,,,,,")
        # result = get_value_array(int(1), last_date, df, tickers)
        # print(registerResult)



def indice_main(Class, Name):
        ticker = Class.TSJ
        tickers = Class.Yahoo #vraie
        if (len(tickers) == 1):
            indice_simple_tickers(ticker, Class, Name)

        else: 
            print("error")
        # print("Error sous hacent")

        for ticker in Class.Yahoo_value_name:
            Class.legende_tickers += "\n" + ticker