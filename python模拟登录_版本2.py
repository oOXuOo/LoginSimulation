#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import http.client

###########################################################
HOST = '210.27.12.1:90'
UserName =  "1302120810"
PassWord =  "1302120810"
data =  "j_username=%s&j_password=%s"        %(UserName,PassWord)
Headers = {
	"Content-Type":"application/x-www-form-urlencoded",
	"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
	}
###########################################################


#连接服务器
conn = http.client.HTTPConnection(HOST,timeout=30)
conn.connect()

#GET到登录页，以获取cookies
conn.request("GET","/j_security_check",None,Headers)
res = conn.getresponse()
m_cookie = res.getheader("Set-Cookie").split(';')[0]
res.read()
 
#POST到登录页，进行登录
Headers["Cookie"] = m_cookie
conn.request("POST","/j_security_check",data,Headers)
res = conn.getresponse()
res.read()
if res.status == 400:
	#再次链接到登录页
	conn.request("POST","/j_security_check",data,Headers)
	res = conn.getresponse()
	res.read()
conn.close()





######################可以开始正常访问啦######################
conn2 = http.client.HTTPConnection(HOST)
conn2.request("GET","/student/index.jsp",None,Headers)
fp = conn2.getresponse()
print(fp.status)
print(fp.read().decode("GBK"))
###########################################################


