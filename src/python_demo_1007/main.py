from pyquery import PyQuery as pq
from savePic import savePic
import urllib.request
 
#爬取地址↓↓↓↓↓
d = pq('https://yande.re/post?page=1') 

#创建文件夹↓↓↓↓↓
createDir('post')

#啪啪啪↓↓↓↓↓
for i in d('#post-list-posts>li>a'):
	print('-------Begin Downing-------')
	#print(i.text())
	i = d(i)
	#link就是jpg的地址了！！！
	link = i.attr('href')
	#print(link)
	print('link-->\n'+link)
	savePic(link, 'post')
	print('-------Get the Pic √-------')
	