
import feedparser
import re


feedlist=[
       'http://www.gentoo.org/rdf/en/gentoo-news.rdf'
        ]


def stripHTML(h):
    p=''
    s=0
    for c in h:
        if c=='<': 
            s=1
        elif c=='>':
            s=0
            p+=' '
        elif s==0:
            p+=c

    return p

def separatewords(text):
    splitter=re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s)>3 ]

def getarticlewords():
    allwords={}
    articlewords=[]
    articletitles=[]
    ec=0

    for feed in feedlist:
        f=feedparser.parse(feed)

        for e in f.entries:
            if e.title in articletitles:
                continue
            txt=e.title.encode('utf8')+stripHTML(e.description.encode('utf8'))
            words=separatewords(txt)
            articlewords.append({})
            articletitles.append(e.title)

            for word in words:
                allwords.setdefault(word,0)
                allwords[word]+=1
                articlewords[ec].setdefault(word,0)
                articlewords[ec][word]+=1

            ec+=1
    return allwords,articlewords,articletitles


