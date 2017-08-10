#NOTES (these functions are to be placed under the data string)
#print(data.EDT) #is used to access number of rows
#data.columns is used to get the column names
#print(data.EDT.head()) gives the first give items in a column. put a value between the head() parenthesis to get the first __ data
#the same applies to .tail() and the dictionary indices too

import pandas
data = pandas.read_csv("weather_year.csv")
from datetime import datetime
import pylab


#this renames the columns
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]
first_date = data.date.values[0]
print (data)
print (data.date.head())
print(first_date)
pylab.show(data.max_temp.tail(20).plot(kind="pie"))

#date.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
#datetime.datetime(2012,3,10,0,0)
