#!/usr/bin/env python3.5

import re
import urllib.request
import os

SAVE_DIR_PATH = 'E:\\temp/'

URL = 'https://mp.weixin.qq.com/s?__biz=MzI1MDA3NDE4NA==&mid=2651069170&idx=2&sn=234aff6c2f9e443f12131d1f8425a8c9#wechat_redirect'


#获得页面内容
def getpage(url):

    my_url=urllib.request.urlopen(url)
    image_page=my_url.read().decode('utf-8')

    return image_page

#获取图片地址
def get_image_url(image_page):

    reg=r'https://pic[0-9].zhimg[^"]*.jpg' #可优化
    image_url=re.compile(reg)
    image_url_list=image_url.findall(image_page)

    return image_url_list


if __name__ == '__main__':
    image_page=getpage(URL)
    image_url_list=get_image_url(image_page)
#下载
for url in image_url_list:
    urllib.request.urlretrieve(url,'%s.png'%image_url_list.index(url))
