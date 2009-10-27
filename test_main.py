##-- coding=utf-8 ##

import newsfeature
from numpy import *
import nmf

allw,artw,artt=newsfeature.getarticlewords()

wordmatrix,wordvec=newsfeature.makematrix(allw,artw)


for i in wordmatrix:
    print i
print "生成的矩阵：",len(i),"x",len(wordmatrix)

v=matrix(wordmatrix)
weights,feat=nmf.factorize(v,pc=20,iter=50)

topp,pn=newsfeature.showfeatures(weights,feat,artt,wordvec)

print topp,pn
