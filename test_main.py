
import newsfeature


allw,artw,artt=newsfeature.getarticlewords()

mat,vec=newsfeature.makematrix(allw,artw)


print "生成的矩阵："len(i),"x",len(mat)
for i in mat:
    print i


