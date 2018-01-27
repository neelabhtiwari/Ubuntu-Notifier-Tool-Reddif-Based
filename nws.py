#coding: utf-8
import urllib2
import re
from bs4 import BeautifulSoup
dt=raw_input('Enter the date in (DD/MM/YYYY) format to view the headlines: ')
print('\n')
print("Following are the headlines for the date %s \n")%dt
print('\n')
ul='http://www.rediff.com/issues/'+dt[0:2]+dt[3:5]+dt[8:]+'hl.html'
quote_page = ul
i=0
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')
fdiv= soup.find_all('div',attrs={'id':'hdtab1'})
for yo in fdiv:
    download = yo.find_all('a',attrs={'target':'_new'})  #href = re.compile('\.htm$')
    for yo in download:
        if i==0:
            hrefText=yo.text[6:]
            i=i+1
        else:
            hrefText=yo.text
        print '-'+hrefText
print('\n')
