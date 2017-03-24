#!/usr/bin/env python
import re, requests
SAVE_DIR_PATH = 'E:\\temp/'
URL = 'http://www.zhihu.com/question/20399991'
save = lambda url: open(SAVE_DIR_PATH + url[url.rfind('/')+1:], 'wb').write(requests.get(url).content)
if __name__ == '__main__':
    map(save, ['http:' + url for url in re.findall(ur'<img src=[\'"](//pic.+?)[\'"].+?>',requests.get(URL).content)])
