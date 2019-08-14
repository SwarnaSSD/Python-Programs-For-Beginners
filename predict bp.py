import matplotlib.pyplot as plt
from pandas import read_csv
import os

# Load data
data_path = os.path.join(os.getcwd(), "DataBase Age Vs B.P.xlsx")
dataset = read_csv(data_path, delim_whitespace=True)

# We have 30 entries in our dataset and four features. The first feature is the ID of the entry.
# The second feature is always 1. The third feature is the age and the last feature is the blood pressure.
# We will now drop the ID and One feature for now, as this is not important.
dataset = dataset.drop(['ID', 'One'], axis=1)

# And we will display this graph
#matplotlib inline
dataset.plot.scatter(x='Age', y='Pressure')

# Now, we will assume that we already know the hypothesis and it looks like a straight line
h = lambda x: 84 + 1.24 * x

# Let's add this line on the chart now
ages = range(18, 85)
estimated = []

for i in ages:
    estimated.append(h(i))

plt.plot(ages, estimated, 'b')  
