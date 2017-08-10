import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)

# Start your search algorithm here.
user_input = input("hey: ")
ord_input = ord(user_input)
for i in countries:
    for char in i:
        var = countries[ord(char)]
        print(var)

##if ord_input = ord()
