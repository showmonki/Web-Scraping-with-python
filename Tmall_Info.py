from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium import webdriver
import time



def get_list(url):
	browser.get(url)
	html = browser.page_source
	print("Load the page")
	simple = BeautifulSoup(html,'html.parser')
	sid = simple.find("div", attrs={'id': 'LineZing'})['shopid']
	sname = simple.select("div.slogo > a > strong")[0].string
	search = simple.find("div", attrs={'data-title': '搜索列表'})
	nodes = search.find_all("dd", attrs={'class': 'detail'})
	#createtime = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(path))).strftime('%Y-%m-%d %H:%M:%S')
	for node in nodes:
		a_click = node.find("a")
		url = str(a_click.get("href"))
		pid = node.parent['data-id']
		pname = node.select("a")[0].string.strip()
		price = node.select("span.c-price")[0].string
		#print(pid, pname, price)
		try:
			time.sleep(15)
			info = get_info(pid)
		except:
			sales = ''
		global df

		df = df.append({'sname': sname,
						'sid': int(sid),
						'pid': int(pid),
						'pname': pname,
						'Info_pname':info['title'],
						'Info_sales': info['sales'][0],
						'sim_price': float(price),
						'promoprice':info['price'],
						'url': url}, ignore_index=True)
		#print(df)


def get_info(pid):
	browser = webdriver.Chrome(executable_path='/Users/nanzou/anaconda3/chromedriver')
	browser.get('https://detail.m.tmall.com/item.htm?id='+pid)
	time.sleep(15)
	print("Load the Info of ", pid)
	html = browser.page_source
	web = BeautifulSoup(html, 'html.parser')
	title = web.select("div.module-title > div.main")[0].string
	price = web.select("div.real-price > span > span.price")[0].string
	sales = re.findall("([0-9]+)",web.select("span.sales")[0].string)
	return{'title':title,
			   'sales':sales,
			   'price':price}

df = pd.DataFrame()
browser = webdriver.PhantomJS(executable_path='/Users/nanzou/anaconda3/phantomjs-2.1.1-macosx/bin/phantomjs')
url='https://skii.tmall.com/search.htm?spm=a1z10.1-b-s.w5001-14630548611.4.3819da66mYXo6M&scene=taobao_shop'
get_list(url)
df.to_excel('/Users/nanzou/SK-II info.xlsx','SK-II')


## get_list: get the product list from Tmall store searching page
## get_info: get the information of each products (Monthly sales, productname, price)
## Finally return the product list with sales information. 
