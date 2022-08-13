import requests
from bs4 import BeautifulSoup

country = input("Enter the country you would like to look up (caps sensitive): ")

res = requests.get("https://www.worldometers.info/coronavirus/country/"+ country)
soup = BeautifulSoup(res.text, 'html.parser')
print("-------------")
for b,i in zip(["Coronavirus Cases","Deaths","Recovered"], soup.findAll('div', { "class" : "maincounter-number" })):
  print (b, i.text)
