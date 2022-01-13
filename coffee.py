import plotly.express as px
import csv
import numpy as np

with open("coffee.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "sleep in hours", y = "Coffee in ml")
    fig.show()

def getDataSrc():
    Coffee = []
    Sleep = []

    with open("coffee.csv") as r:
        csvReader = csv.DictReader(r)
        
        for row in csvReader:
            Coffee.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))
    
    return{"x":Sleep, "y":Coffee}

def findCorrelation(dataSrc):
    Correlation = np.corrcoef(dataSrc["x"], dataSrc["y"])
    print("the Correlation between Coffee and Sleep is:", Correlation[0,1])

def setup():
    dataSrc = getDataSrc()
    findCorrelation(dataSrc)

setup()
    
        
