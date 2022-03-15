import requests

#file = requests.get('https://covid.ourworldindata.org/data/jhu/full_data.csv')
#open('full_data.csv', 'wb').write(file.content)

lines = open('full_data.csv').readlines()
data = lines[2]
d = data.split(',')
d.remove(d[-1])
print(d)