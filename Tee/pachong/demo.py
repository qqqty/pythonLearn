import re
import urllib


def getHtml(url):
    obj = urllib.urlopen(url)
    html = obj.read()

    return html


def getImg(html):

    reg = r'src="(.+?\.jpg)" pic_ext'
    imgRe = re.compile(reg)
    imgList = re.findall(imgRe, html)

    return imgList


def downImg(imgList):
    x = 0
    for imgUrl in imgList:
        savePath = 's/%s.jpg' % x
        urllib.urlretrieve(imgUrl, savePath)
        print '%d success' % x
        x += 1
        if x >= 5:
            break

    return True

url = "http://tieba.baidu.com/p/2460150866"
html = getHtml(url)
imgList = getImg(html)
downImg(imgList)




# #--------------abc----------------------------
#
# import urllib
# def callbackfunc(blocknum, blocksize, totalsize):
#
#     percent = 100.0 * blocknum * blocksize / totalsize
#     if percent > 100:
#         percent = 100
#     print "%.2f%%" % percent
#
# url = 'http://www.sina.com.cn'
# local = 's/a.html'
# urllib.urlretrieve(url, local, callbackfunc)































