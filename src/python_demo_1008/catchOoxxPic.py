from html_withUA_method1 import *
from savePic import *
from pyquery import PyQuery as pq


pageSearch = 10 #设置要爬取的页数

maxNum = None #ooxx的最大页数

def main():
	page = list(range(1,maxNum+1))
	#从最大页数开始爬, 100->1
	pageUse = page[::-1][:pageSearch]
	createDir('pic')
	#print(pageUse)
	for i in pageUse:
		stri = str(i)
		print('Starting Page' + stri +'\'s Download')
		url = 'http://jandan.net/ooxx/page-' + stri
		html = getHtml(url)
		html_content = pq(html)
		saveDir = 'pic\\' + stri
		createDir(saveDir)
		for p in html_content('li p>img').items():
			if p.attr('org_src') != None:
				pass
				savePic(p.attr('org_src'),saveDir)
			else :
				pass
				savePic(p.attr('src'),saveDir)
		print('Ending Page' + stri +'\'s Download')

def getMax():
	url = 'http://jandan.net/ooxx'
	html = getHtml(url)
	html_content = pq(html)
	maxNum = html_content('.current-comment-page:first').text()
	#print(maxNum[1:-1])
	return maxNum[1:-1]

#data = getHtml("")
if __name__ == '__main__':
	maxNum = int(getMax())
	main()
