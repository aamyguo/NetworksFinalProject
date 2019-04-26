from requests import get
from bs4 import BeautifulSoup

class Search():
	def Trending():
		url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
		response = get(url)
		html_soup = BeautifulSoup(response.text, 'html.parser')
		#type(html_soup)
		arr = []

		trend_containers = html_soup.find_all('title')
		#print(type(trend_containers))
		#print(len(trend_containers))


		for i in range(1,len(trend_containers)):
			#print(trend_containers[i].get_text())
			arr.append(trend_containers[i].get_text())
		#print(arr)
		return arr

print(Search.Trending())
