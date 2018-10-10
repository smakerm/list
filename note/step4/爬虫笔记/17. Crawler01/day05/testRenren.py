# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:10:55 2018

@author: Administrator
"""

import urllib

#anonymid=jhlopkol7jjtbs; depovince=BJ; jebecookies=598ed5ea-874b-4d3c-8cd4-be09fe30b407|||||; _r01_=1; JSESSIONID=abc1qnh7W5WwRc0b5vwow; ick_login=723cae2a-c57b-400f-93e1-3c2b006de3d4; jebe_key=b43d7595-4355-434f-bd34-411ed0e3a7b9%7C65617699d9107c4fa92a82edbc369e2a%7C1527236707731%7C1%7C1527236506627; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; _de=7113E26C6AAF3646A83FD76533146E3C; p=618fd9a4f10e78c0189b16848a0462be9; t=d455a8e8e214d69f3e72c64123d059b49; societyguester=d455a8e8e214d69f3e72c64123d059b49; id=961482489; xnsid=6999487e; ch_id=10016; wp_fold=0
url = "http://www.renren.com/961482489/profile"

ua_headers = {"Cookie":"anonymid=jhlopkol7jjtbs; depovince=BJ; jebecookies=598ed5ea-874b-4d3c-8cd4-be09fe30b407|||||; _r01_=1; JSESSIONID=abc1qnh7W5WwRc0b5vwow; ick_login=723cae2a-c57b-400f-93e1-3c2b006de3d4; jebe_key=b43d7595-4355-434f-bd34-411ed0e3a7b9%7C65617699d9107c4fa92a82edbc369e2a%7C1527236707731%7C1%7C1527236506627; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; _de=7113E26C6AAF3646A83FD76533146E3C; p=618fd9a4f10e78c0189b16848a0462be9; t=d455a8e8e214d69f3e72c64123d059b49; societyguester=d455a8e8e214d69f3e72c64123d059b49; id=961482489; xnsid=6999487e; ch_id=10016; wp_fold=0",
              "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
              "Connection":"keep-alive",
              "Host":"www.renren.com"
              }

req = urllib.request.Request(url, headers=ua_headers)
response = urllib.request.urlopen(req)

with open("myRenren.html", "wb") as f:
    f.write(response.read())
