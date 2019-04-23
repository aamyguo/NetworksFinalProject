#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Searches.py
#  
#  Copyright 2019 Ashten <Ashten@NOAH-HP>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

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


print ("Hello Wold")
for i in range(0,5):
	print(i)
