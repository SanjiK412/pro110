import plotly.figure_factory as ff 
import csv
import pandas as pd 
import statistics
import random

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
print(population_mean)
fig=ff.create_distplot([data], ["reading_time"], show_hist=False)
#fig.show()
standard_deviation=statistics.stdev(data)
print(standard_deviation)

def random_set(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    samplemean=statistics.mean(dataset)
    samplestandard_deviation=statistics.stdev(dataset)
    return samplemean

def show_fig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,30):
        randommean=random_set(99)
        mean_list.append(randommean)
    show_fig(mean_list)
setup()
