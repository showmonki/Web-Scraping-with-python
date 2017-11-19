from bs4 import BeautifulSoup
import re
import urllib
import pandas as pd
from selenium import webdriver
import time



def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def get_news(url):
	html=getHtml(url)
	web=BeautifulSoup(html,'html.parser')
	search = web.find("div", attrs={'class': 'list1 list_wz'})
	content=web.find("div",attrs={'id':'detailContent'})
	nodes = search.find_all("p")
	for node in nodes:
		link=node.find("a").get("href")
		title=node.find("a").string
		post_time=node.find("span").string.replace("\n","").replace('\t',"").replace('\r',"").strip()
		full=("http://www.ihepa.com:8088"+link)
		if post_time>'2017-03-01' and post_time<'2017-08-31':
			detail=get_content(full)
			time.sleep(3)
			global df
			df = df.append({'link': full,
							'title': title,
							'content': detail,
							'time': post_time}, ignore_index=True)
			print(title)
		else: continue




def get_content(url):
	browser = webdriver.PhantomJS(executable_path='/Users/nanzou/anaconda3/phantomjs-2.1.1-macosx/bin/phantomjs')
	browser.get(url)
	time.sleep(5)
	html = browser.page_source
	web = BeautifulSoup(html, 'html.parser')
	detail = web.find("div", attrs={'id': 'detailContent'})
	pattern = re.compile(r'\<.*?\>' )
	content=pattern.sub("",str(detail)).replace("\n","").replace('\t',"").strip()
	return content

df = pd.DataFrame()
url='http://www.ihepa.com:8088/tags/bz/6?pager.offset=20'
get_news(url)
df.to_excel('C:\\Users\\User\\Desktop\\BMS.xlsx','page2')

