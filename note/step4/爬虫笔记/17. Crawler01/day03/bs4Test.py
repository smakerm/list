# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:17:41 2018

@author: Administrator
"""

from bs4 import BeautifulSoup
doc=['<html><head><title>Page title</title></head>',
     '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.</p>',
     '<p id="secondpara" align="center">This is paragraph <b>two</b>.</p></body>',
     '</html>']
soup = BeautifulSoup(''.join(doc),"html.parser")
#print(type(soup)) # <class 'bs4.BeautifulSoup'>
#print(soup.prettify())
#<html>
# <head>
#  <title>
#   Page title
#  </title>
# </head>
# <body>
#  <p align="center" id="firstpara">
#   This is paragraph
#   <b>
#    one
#   </b>
#   .
#   <p align="blah" id="secondpara">
#    This is paragraph
#    <b>
#     two
#    </b>
#    .
#   </p>
#  </p>
# </body>
#</html>

#html = soup.contents[0]
#print(html.name) # tag name
#
#head = soup.contents[0].contents[0]
#print(head.name)
#
#body = soup.contents[0].contents[1]
#print(body.name)

items = soup.findAll('p', id="firstpara")
for it in items:
    print(it.text)
#<p align="center" id="firstpara">This is paragraph <b>one</b>.</p>    

