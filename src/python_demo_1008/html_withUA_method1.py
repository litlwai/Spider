import urllib.request
from pyquery import PyQuery as py
import savePic

#get this method from 
#http://jecvay.com/2014/09/python3-web-bug-series3.html

def getHtml(url):
	req = urllib.request.Request(url,headers={
		'Connection': 'Keep-Alive',
    	'Accept': 'text/html, application/xhtml+xml, */*',
    	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
	})

	oper = urllib.request.urlopen(req)
	html = oper.read()
	return html


#savePic.createDir('1570')

#html_content = py(data)
#print(html_content('table>thead>tr>th'))

#for i in html_content('li p>img').items():
	#print(type(i))
	#i = html_content(i)
	#if i.attr('org_src') != None:
		#pass
		#savePic.savePic(i.attr('org_src'),'1570')
	#else :
		#pass
		#savePic.savePic(i.attr('src'),'1570')

#file = open('ooxxpage1-decode.txt','wb')
#file.write(data.decode())
#file.close()
#print(data.decode())