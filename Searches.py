
# import libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

#url
quote_page = 'https://trends.google.com/trends/trendingsearches/daily?geo=US'
# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
for i in range(len(soup.find_all('div class = "title title-break"'))):
	print(soup.find_all('div class = "title title-break"')[i].get_text())
#print(soup.get_text())
"""
# Take out the <div> of name and get its value
name_box = soup.find('span', attrs ={'ng-repeat': 'titlePart in titleArray'})
#name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name_box.get_text())
"""
