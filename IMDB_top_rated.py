import requests
from bs4 import BeautifulSoup
import html5lib
import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "top rated movies"
print (excel.sheetnames)
sheet.append(['rank','name','rating','year'])

url = "https://www.imdb.com/chart/top/"
#REQUESTING THE WEBPAGE TO RETRIEVE IT'S HTML CONTENT
content = requests.get(url)
#THIS IS USED TO CHECK IF THE URL PROVIDED IS TRUE OR NOT
content.raise_for_status()
#PARSING THE HTML FILE
soup = BeautifulSoup(content.text, 'html.parser')
soup.prettify
try:
 movies = soup.find('tbody', class_="lister-list").find_all('tr')
 for movie in movies:
     name = movie.find('td', class_="titleColumn").a.text
     
     rank = movie.find('td', class_="titleColumn").text.strip().split('.')[0]

     rating = movie.find('td', class_="ratingColumn imdbRating").text

     year = movie.find('td', class_="titleColumn").span.text.strip('()')
     print(rank, name, rating, year)
     sheet.append([rank, name, rating, year])

except Exception as e:
  print(e)     

excel.save("TOP RATED MOVIES.xlxs")