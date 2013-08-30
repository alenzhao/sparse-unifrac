#!/usr/bin/env python

import numpy
from tree import readtree

def unifrac_mix(As,otusid,t):
#unifracc a partir de una matriz sparse pero luego utilizando slice de columna densos al comparar muestras
    As.convert('csc')
    m , n = As.shape
    dist_vec,pos = readtree(t,otusid)
    dist = numpy.zeros([n,n])
    x = numpy.zeros(m,bool)
    x[As._unpkd_ax[As._pkd_ax[0]:As._pkd_ax[1]]] = True
    x = dev_vec(pos,x)
    for i in range(n):
        for j in range(n-1,i,-1):
            y = numpy.zeros(m,bool)
            y[As._unpkd_ax[As._pkd_ax[j]:As._pkd_ax[j + 1]]] = True
            y = dev_vec(pos,y)
            dist[i,j] = dist[j,i] = calc_dist3(x,y,dist_vec)
        x = y
    return dist

def unifrac_mix_weighted(As,otusid,t,s):
    As.convert('csc')
    m , n = As.shape
    dist_vec,pos = readtree(t,otusid)
    dist = numpy.zeros([n,n])
    x = numpy.zeros(m)
    x[As._unpkd_ax[As._pkd_ax[0]:As._pkd_ax[1]]] = As._values[As._pkd_ax[0]:As._pkd_ax[1]]
    x = dev_vec_weighted(pos,x)
    sx = s[0]
    for i in range(n):
        for j in range(n-1,i,-1):
            y = numpy.zeros(m)
            y[As._unpkd_ax[As._pkd_ax[j]:As._pkd_ax[j + 1]]] = As._values[As._pkd_ax[j]:As._pkd_ax[j + 1]]
            sy = s[j]
            y = dev_vec_weighted(pos,y)
            dist[i,j] = dist[j,i] = calc_dist_weighted(x,y,dist_vec,sx,sy)
        x = y
        sx = sy
    return dist

def unifrac_mix_weighted2(As,otusid,t):
    As.convert('csc')
    m , n = As.shape
    dist_vec,pos = readtree(t,otusid)
    dist = numpy.zeros([n,n])
    x = numpy.zeros(m)
    x[As._unpkd_ax[As._pkd_ax[0]:As._pkd_ax[1]]] = As._values[As._pkd_ax[0]:As._pkd_ax[1]]
    sx = sum(x)
    x = dev_vec_weighted(dist_vec,pos,x)    
    for i in range(n):
        for j in range(n-1,i,-1):
            y = numpy.zeros(m)
            y[As._unpkd_ax[As._pkd_ax[j]:As._pkd_ax[j + 1]]] = As._values[As._pkd_ax[j]:As._pkd_ax[j + 1]]
            sy = sum(y)
            y = dev_vec_weighted(dist_vec,pos,y)
            dist[i,j] = dist[j,i] = calc_dist_weighted(x,y,dist_vec,sx,sy)
        x = y
        sx = sy
    return dist

def dev_vec(pos,v):
#calcula el valor de una unica muestra en los nodos interiores para un vector denso
    m = len(v)
    l = len(pos)
    aux = numpy.zeros(m+l,bool)
    aux[0:m] = v
    for i in range(l):
        aux[i+m] = numpy.logical_or.reduce(aux[pos[i]])
    return aux

def calc_dist(x,y,dist_vec):
    xy = numpy.logical_and(x,y).astype(int)
    sumx = ((x-xy) * dist_vec).sum()
    sumy = ((y-xy) * dist_vec).sum()
    sumxy = (xy * dist_vec).sum()
    return (sumx + sumy)/(sumx + sumy + sumxy)

def calc_dist2(x,y,dist_vec):
    xor = numpy.logical_xor(x,y)
    o = numpy.logical_or(x,y)
    sumxor = (xor * dist_vec).sum()
    sumor = (o * dist_vec).sum()
    return sumxor/sumor

def calc_dist3(x,y,dist_vec):
    xor = numpy.logical_xor(x,y)
    o = numpy.logical_or(x,y)
    sumxor = numpy.dot(xor,dist_vec)
    sumor = numpy.dot(o,dist_vec)
    return sumxor/sumor

def dev_vec_weighted(pos,v):
    m = len(v)
    l = len(pos)
    aux = numpy.zeros(m+l,int)
    aux[0:m] = v
    for i in range(l):
        aux[i+m] = aux[pos[i][0]] + aux[pos[i][1]]
    return aux

def calc_dist_weighted(x,y,dist_vec,sx,sy):
    aux = abs(x.astype(float)/sx - y.astype(float)/sy)
    s = sum(aux*dist_vec)
    return s

def sum_dict(dic):
    m,n = dic.shape
    s = numpy.zeros(n,int)
    for i in range(n):
        for ((j,k),x) in dic.getCol(i).iteritems():
            s[i] += x
    return s
