import plotly.express as px
import csv
import numpy as np

with open("marks.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
    fig.show()

def getDataSrc():
    marksInPercentage = []
    daysPercentage = []

    with open("marks.csv") as r:
        csvReader = csv.DictReader(r)
        
        for row in csvReader:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            daysPercentage.append(float(row["Days Present"]))
    
    return{"x":marksInPercentage, "y":daysPercentage}

def findCorrelation(dataSrc):
    Correlation = np.corrcoef(dataSrc["x"], dataSrc["y"])
    print("the Correlation between Marks and Days is:", Correlation[0,1])

def setup():
    dataSrc = getDataSrc()
    findCorrelation(dataSrc)

setup()
    
        
