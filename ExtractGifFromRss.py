from urllib2 import urlopen
import bs4 as BeautifulSoup
import feedparser
import webbrowser
import urllib
import os.path
import schedule
import time
import datetime
from datetime import date

LastParsedDate = datetime.datetime.utcnow()
GifDirectory = "../Gif"
RssFlux = 'http://Forexample/atom.xml'


def DownloadGif(gifImage) :
    global GifDirectory
    filename=gifImage.split('/')[-1]
    filePath = GifDirectory + "/" + filename
    if os.path.isfile(filePath) == False :
        print "Download :" + filename + " ..."
        urllib.urlretrieve(gifImage, filePath)    

def job():   
    global LastParsedDate 
    
    print str(datetime.datetime.utcnow())  + " : The Gif Extractor is working..."


    if os.path.isdir(GifDirectory) == False :
        os.mkdir(GifDirectory)   
        
    newDateCheck = datetime.datetime.utcnow()
    flux = feedparser.parse(RssFlux)

    for entry in flux.entries :
        if entry.published_parsed > LastParsedDate.utctimetuple() :
            html = urlopen(entry.link).read()
            datePublished = str(datetime.datetime(*entry.published_parsed[:6]))
            print " New Publication : " + datePublished + " : " + entry.link
            soup = BeautifulSoup.BeautifulSoup(html)

            for div in soup.findAll('img'):
                if div['src'].endswith(".gif") :
                    gifImage = div['src']
                    DownloadGif(gifImage)

    LastParsedDate = newDateCheck


schedule.every(1).hours.do(job)
job()


while True:
    schedule.run_pending()
    time.sleep(1)
