import urllib.request
import os
 
#流程:读取图片->获取文件名(网址最后的'/'的后面那部分)->写入图片

#当前目录路径
dirname = os.path.abspath(os.path.dirname(__file__))

def savePic(url, saveDir):
	jpg_data = urllib.request.urlopen(url).read()	#读取图片
	splitPath = url.split('/')
	fName = splitPath.pop() #获取文件名(网址最后的'/'的后面那部分)

	f = open(dirname+'\\'+saveDir+'\\'+fName, 'wb')	
	f.write(jpg_data)	#写入图片
	f.close()

def createDir(saveDir):
	if not os.path.exists(saveDir):
		os.mkdir(saveDir)	#在当前目录下新建一个存放图片的文件夹


#__file__：当前文件名
#os.path.dirname(file): 某个文件所在的目录路径
#os.path.join(a, b, c,....): 路径构造 a/b/c
#os.path.abspath(path): 将path从相对路径转成绝对路径
#os.pardir: Linux下相当于"../"
#print (os.path.abspath(os.path.dirname(__file__)))


#读取图片
#url = "http://ww3.sinaimg.cn/mw600/4bf31e43jw1ewsekw0k1qj20m80xc468.jpg"
#jpg_data = urllib.request.urlopen(url).read()

#获取文件名
#splitPath = url.split('/')
#fName = splitPath.pop()
#print(fName)

#写入图片
#if not os.path.exists('test'):
#	os.mkdir('test')
#f = open(dirname+'\\'+'\\'+fName, 'wb')
#f.write(jpg_data)
#f.close()