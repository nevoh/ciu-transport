from bs4 import BeautifulSoup
import requests
from requests.api import request

url = 'https://www.ciu.edu.tr/service-hours'

result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

bus_info = {}
bus_schedule = {}
lst = []


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


columns = doc.find_all(class_='column')

for column in columns:
    day = column.find(class_='column-title').text
    print(day)
    for schedule in column.find_all(class_='line-style'):
        time = schedule.text.split('(')[0].replace(' ', '')
        bus_no = schedule.text[schedule.text.find(
            '(')+1:schedule.text.find(')')]
        lst.append(time)
        lst.append(bus_no)
        bus_info[day] = Convert(lst)
print(bus_info['SATURDAYS']['21:30'])
