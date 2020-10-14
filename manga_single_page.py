import ssl

ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver
import time



def getHtml(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'}
	html_req = req.Request(url,headers=headers)
	page = req.urlopen(html_req)
	html = page.read()
	#browser = webdriver.PhantomJS(executable_path='/Users/nanzou/anaconda3/phantomjs-2.1.1-macosx/bin/phantomjs')
    #browser.get(url)
    #time.sleep(1)
	#html = browser.page_source
	return html


def click_1_ep(url,loc):
	#html=getHtml(url)
	#web=BeautifulSoup(html,'html.parser')
	#search = web.find("div", attrs={'class': 'listboxpic'})
	#start = search.find("li")
	#link=start.find("a").get("href")
	while True:
		time.sleep(3)
		browser = webdriver.PhantomJS(executable_path='/Users/nanzou/anaconda3/phantomjs-2.1.1-macosx/bin/phantomjs',service_args=['--ssl-protocol=any','--ignore-ssl-errors=true'])
		url = down_pic_1_ep(url,browser)


def down_pic_1_ep(url,browser):
	browser.get(url)
	time.sleep(1)
	html = browser.page_source
	web = BeautifulSoup(html, 'html.parser')
	cartoon_page = web.find("div", attrs={'class': 'cartoon-page'})
	try:
		thisclass = cartoon_page.find("li",attrs={'class':'thisclass'})
	except AttributeError:
		print("Download to latest episode")
		exit()
	pic = web.find("div", attrs={'class': 'cartoon-content'})
	title = pic.find("h2").string
	pic_link=pic.find("img").get("src")
	pic_file = getHtml(pic_link)
	print("Saving "+title)
	with open(save_loc + "/" +title+"_"+'.png',"wb") as file:
		file.write(pic_file)
	if thisclass.find_next_sibling().find("a").get("href") !="#":
		return "http://www.myherocn.com/manhua/"+thisclass.find_next_sibling().find("a").get("href")
	else:
		print("Finish this episode, Get next episode")
		return "http://www.myherocn.com"+web.find("li",attrs={"class":"next"}).find("a").get("href")



url="http://www.myherocn.com/manhua/"+input('paste the number of episode gonna download this time\n')+".shtml"
save_loc = "/transfer/manga"
click_1_ep(url,save_loc)

