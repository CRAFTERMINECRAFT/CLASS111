from os import makedirs, name
import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
import random
import plotly.graph_objects as go


df = pd.read_csv("maths.csv")
data = df["Math_score"].tolist()


popMean = statistics.mean(data)
popSD = statistics.stdev(data)


print("\n")
print("Mean is ", popMean)
print("standard deviation is", popSD)
print("\n")


def randomMean(c):
    dataset = []
    for i in range(0,c):
        ri = random.randint(0,len(data)-1)
        value = data[ri]
        dataset.append(value)
    smean = statistics.mean(dataset)
    return smean


def figShow(l):
    df = l
    fig = ff.create_distplot([df],["Math_score"],show_hist=False)
    fig.show()


def main():
    meanList =[]
    for i in range(0,1000):
        m = randomMean(100)
        meanList.append(m)
    mm = statistics.mean(meanList)
    msd = statistics.stdev(meanList)
    print("\n")
    print("Mean of mean is ", mm)
    print("standard deviation of mean is", msd)
    print("\n")


    #figShow(meanList)


    sample1 = pd.read_csv("d3.csv")
    data1 = sample1["Math_score"].tolist()
    samm = statistics.mean(data1)
    z = (samm - mm) / msd
    print(z)

    firstsd = mm + msd
    secondsd = mm + (2*msd)
    thirdsd = mm+ (3*msd)
    fig1 = ff.create_distplot([meanList], ["Marks"], show_hist = False)
    fig1.add_trace(go.Scatter(x = [mm,mm], y = [0,0.17], mode = "lines", name = "Mean"))
    fig1.add_trace(go.Scatter(x = [firstsd,firstsd], y = [0,0.17], mode = "lines", name = "First SD"))
    fig1.add_trace(go.Scatter(x = [secondsd,secondsd], y = [0,0.17], mode = "lines", name = "Second SD"))
    fig1.add_trace(go.Scatter(x = [thirdsd,thirdsd], y = [0,0.17], mode = "lines", name = "Third SD"))
    fig1.add_trace(go.Scatter(x = [samm,samm], y = [0,0.17], mode = "lines", name = "Sample Mean"))
    fig1.show()

main()