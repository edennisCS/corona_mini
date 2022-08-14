import requests
from bs4 import BeautifulSoup

def look_up():
  country = input("Enter the country you would like to look up [China, Italy, Iran, Spain, Germany, South-korea, France, USA or UK]: ")
  
  if country.upper() == "USA":
    country = "us"
  try:
    res = requests.get("https://www.worldometers.info/coronavirus/country/"+ country.lower())
  except:
    try:
      res = requests.get("https://www.worldometers.info/coronavirus/country/"+ country.upper())
    except:
      print("Sorry, please try another query.")

        

  soup = BeautifulSoup(res.text, 'html.parser')
  print("-------------")
  for b,i in zip(["Coronavirus Cases","Deaths","Recovered"], soup.findAll('div', { "class" : "maincounter-number" })):
    print (b, i.text)
  print(" ")