
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

def makematrix(allw,articlew):
    wordvec=[]

    for w,c in allw.items():
        if c>3 and c<len(articlew)*0.6:
            wordvec.append(w)

    l1=[[(word in f and f[word] or 0) for word in wordvec] for f in articlew]
    
    return l1,wordvec

from numpy import *

def showfeatures(w,h,titles,wordvec,out='feature.txt'):
    outfile=file(out,'w')
    pc,wc=shape(h)
    toppatternnames=[[] for i in range(len(titles))]
    patternnames=[]

    for i in range(pc):
        slist=[]

        for j in range(wc):
            slist.append((h[i,j],wordvec[j]))

        slist.sort()
        slist.reverse()

        n=[s[1] for s in slist[0:6]]
        outfile.write(str(n)+'\n')
        patternnames.append(n)

        flist=[]

        for j in range(len(titles)):
            flist.append((w[j,i],titles[j]))
            toppatternnames[j].append((w[j,i],i,titles[j]))

        flist.sort()
        flist.reverse()

        for f in flist[0:3]:
            outfile.write(str(f)+'\n')
        outfile.write('\n')

    outfile.close()

    return toppatternnames,patternnames
