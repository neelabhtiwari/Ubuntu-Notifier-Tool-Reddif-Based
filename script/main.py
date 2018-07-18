#coding: utf-8
import urllib2
from bs4 import BeautifulSoup
import notify2
import time
from datetime import date
import os

cwd = os.getcwd()
#print(cwd)

det=date.today()
dt=str(det)

icons=[cwd+"/nwsicn.png",cwd+"/crcicn.png",cwd+"/stkicn.png"]

while 1:
    ul='http://www.rediff.com/issues/'+dt[8:]+dt[5:7]+dt[2:4]+'hl.html'
    quote_page = ul
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page,'html.parser')
    fdiv= soup.find_all('div',attrs={'id':'hdtab1'})
    for yo in fdiv:
        download = yo.find_all('a',attrs={'target':'_new'})
        i=0
        for yo in download:
            if i==0:
                hrefText=yo.text[6:]
                tit='BREAKING'
                notify2.init("Ubuntu News Notifier")
                nn=notify2.Notification(tit,hrefText,icons[0])
                nn.set_urgency(notify2.URGENCY_LOW)
                nn.set_timeout(1000)
                nn.show()
                time.sleep(10)
                i=i+1;
            elif i<6:
                hrefText=yo.text
                tit='Recent'
                notify2.init("Ubuntu News Notifier")
                nn=notify2.Notification(tit,hrefText,icons[0])
                nn.set_urgency(notify2.URGENCY_LOW)
                nn.set_timeout(1000)
                nn.show()
                time.sleep(10)
                i=i+1

    start=0

    while start!=18:
        start=start+1
        ul="http://www.bseindia.com/Msource/IndexMovers.aspx?ln=en"
        page = urllib2.urlopen(ul)
        soup = BeautifulSoup(page,'html.parser')
        data = soup.text
        allstocks=data.split(",")
        title=allstocks[0].split(";")[0]+' '+allstocks[0].split(";")[1]
        newsensexvalue=allstocks[1]
        valchange=allstocks[2]
        perchange=allstocks[3]
        hrefText=newsensexvalue+'\n'+valchange+'  '+perchange+'%'
        #print(hrefText)
        notify2.init("Ubuntu BSE Notifier")
        nn=notify2.Notification(title,hrefText,icons[2])
        nn.set_urgency(notify2.URGENCY_LOW)
        nn.set_timeout(1000)
        nn.show()
        time.sleep(10)
        time.sleep(180)

    time.sleep(60)
