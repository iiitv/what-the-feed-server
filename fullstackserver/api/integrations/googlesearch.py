from urllib import request
import re
from bs4 import BeautifulSoup
# Search google, match links by regex, return the links, integration functions get names from links

"""
Function to return links from google search
https://github.com/aviaryan/pythons/blob/master/Others/GoogleSearchLinks.py
"""
def googleSearchLinks(search):
	name = search
	name  = name.replace(' ','+')
	url = 'http://www.google.com/search?q=' + name
	req = request.Request(url, headers={'User-Agent' : "foobar"})
	response = request.urlopen(req)
	html = response.read()
	soup = BeautifulSoup(html.decode(errors='replace'), 'lxml') # phast
	links = []
	for h3 in soup.find_all('h3'):
		link = h3.a['href']
		link = re.sub(r'^.*?=', '', link, count=1) # prefixed over links \url=q?
		link = re.sub(r'\&sa.*$', '', link, count=1) # suffixed google things
		links.append(link) # link
		#print(h3.get_text()) # text
	return links