
import newsfeature


allw,artw,artt=newsfeature.getarticlewords()

mat,vec=newsfeature.makematrix(allw,artw)


for i in mat:
    print i
print len(i),"x",len(mat)

print len(vec),vec
