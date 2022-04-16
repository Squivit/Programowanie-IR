from matplotlib import type1font
import requests
import matplotlib.pyplot as plt

#file = requests.get('https://covid.ourworldindata.org/data/jhu/full_data.csv')
#open('full_data.csv', 'wb').write(file.content)

locations = []
cases = {}
with open('full_data.csv') as file:
    for line in file:
        loc = line.split(',')[1]
        if not locations.__contains__(loc):
            locations.append(loc)

print(*locations)

loc = input('Podaj nazwę kraju, którego dane chcesz zobaczyć: ')

with open('full_data.csv') as file:
    for line in file:
        data = line.split(',')[:3]
        if data[1] == loc:
            cases[data[0]] = data[2]

x = list(cases.keys())
y= list(map(float, cases.values()))
plt.axes(xlabel='data, pierwszy rok', ylabel='liczba zachorowań',
xticks=[60*i for i in range(int(len(x)/60))],
yticks=[1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000,50000,55000,60000,65000])
plt.plot(x, y, c='red',marker='')
plt.show()
