import pandas
data = pandas.read_csv("bagel.csv")
from datetime import datetime
import pylab

pylab.show(data.plot(kind="pie"))
