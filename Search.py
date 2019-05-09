#pip install beautifulsoup4
#pip install google
#pip install selenium

from requests import get
from bs4 import BeautifulSoup
import webbrowser
#from selenium import webdriver
#import selenium
#from time import sleep

class Search():
	def Trending():
		url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
		response = get(url)
		html_soup = BeautifulSoup(response.text, 'html.parser')
		arr = []
		trend_containers = html_soup.find_all('title')
		for i in range(1,len(trend_containers)):
			arr.append(trend_containers[i].get_text())
		return arr

tren = Search.Trending()

#Tries to get a google search connection
try: 
	from googlesearch import search 
except ImportError:  
	print("No module named 'google' found") 

#Loops over array of trending searches and performs a websearch 
for i in range(0,len(tren)):
	query = tren[i]
	for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
		print(j) 
		
		#driver = webdriver.PhantomJS(executable_path=r'C:\Users\Ashten\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs')
		#driver = webdriver.Chrome(executable_path=r'C:\Users\Ashten\Downloads\chromedriver_win32\chromedriver.exe')
		#driver.get(j)
		#sleep(2)
		#driver.close()
		
	
