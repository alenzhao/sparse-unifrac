#!/usr/bin/env python

#otusid lista con la id de los otus de cada fila, A 0 y 1 en int, t Netwick

import numpy

def readtree(t,otusid):
#lee el arbol y da un vector con las distancias a tener en cuenta para cada nodo y otro vector pos que indica, para cada nodo interno a tener en cuenta, el indice de sus nodos child en la matriz 
    if len(otusid)==0:
        raise ValueError("Otus id cannot be void")
    elif len(otusid)==1:
        intnodespos = []
        for x in t.tips():
            if x.getNodeNames()[0] in otusid:
                break
        dist = numpy.array([x.distance(t)])
    else:
        m = len(otusid)
        dist = numpy.zeros(m)
        ytip = 0
        yint = 0
        firsttip = True
        firstint = True
        newnodes = []
        newnodesind = []
        intnodespos = []
        for x in t.postorder():
            if x.istip():
                if x.getNodeNames()[0] in otusid:
                    indx = otusid.index(x.getNodeNames()[0])
                    if firsttip:
                        dist[indx] = 1
                        firsttip = False
                    else:
                        last = x.lastCommonAncestor(ytip)
                        dist[indx] = x.distance(last)
                        dist[indy] = min(dist[indy],ytip.distance(last))
                        newnodes.append(last)
                        newnodesind.append([indx,indy])
                    indy = indx
                    ytip=x
            else:
                if x in newnodes:
                    ix = newnodes.index(x)
                    if not firstint:
                        lasti = x.lastCommonAncestor(yint)
                        if lasti == x:
                            dist = numpy.hstack((dist,yint.distance(x)))
                            intnodespos.append(newnodesind[iy])
                            refresh_index(newnodesind[ix],newnodesind[iy],m + len(intnodespos) - 1,x,yint)
                        else:
                            dist = numpy.hstack((dist,yint.distance(lasti)))
                            il = newnodes.index(lasti)
                            intnodespos.append(newnodesind[iy])
                            newnodesind[il][1] = m + len(intnodespos) - 1
                            newnodesind[il][0] = m + len(intnodespos)
                    else:
                        firstint = False
                    yint = x
                    iy = ix
        dist[indy] = min(dist[indy],ytip.distance(last))
        dist = numpy.hstack((dist,yint.distance(t)))
        intnodespos.append(newnodesind[iy])
    return dist,intnodespos

def refresh_index(ind1,ind2,pos,x,y):
    if y.tips()[0] in x.Children[0].tips():
        ind1[1] = pos
    if y.tips()[0] in x.Children[1].tips():
        ind1[0] = pos
    if len(x.Children)>2:
        if y.tips()[0] in x.Children[2].tips():
            ind1.append(pos)        


