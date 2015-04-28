#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar

StudentInfoURL = 'http://210.27.12.1:90/student/index.jsp'
loginURL = 'http://210.27.12.1:90/login.jsp'
loginCheckURL = 'http://210.27.12.1:90/j_security_check'
post_data = urllib.parse.urlencode({'j_username': '1302120810', 'j_password': '1302120810'})
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'UserAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36'
}

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#此处一定要链接一次，否则得不到cookie
opener.open(loginCheckURL)	
urllib.request.install_opener(opener)


######################此处加入异常处理，再登一次即可######################
request = urllib.request.Request(loginCheckURL, post_data, headers)
try:
	response = urllib.request.urlopen(request)
except:
	response = urllib.request.urlopen(request)
print(response.read().decode('GBK'))


######################可以开始正常访问啦######################
request = urllib.request.Request(StudentInfoURL, headers=headers)
fp =  urllib.request.urlopen(request)
print(fp.read().decode('GBK'))
