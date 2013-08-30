#!/usr/bin/env python

import numpy
from cogent.util.unit_test import TestCase, main
from cogent.parse.tree import DndParser
from cogent.maths.unifrac.fast_tree import UniFracTreeNode
from sparse_unifrac.tree import readtree

class ReadTreeTests(TestCase):

    def setUp(self):
        self.tree = DndParser('((a:0.1,(b:0.13,c:0.17):0.08):0.09,(d:0.21,e:0.24):0.11)',UniFracTreeNode)
        """
                    /-a
          /--------|
         |         |          /-b
         |          \--------|
---------|                    \-c
         |
         |          /-d
          \--------|
                    \-e

        """

    def test_completeread(self):
        otusid = ['a','b','c','d','e']
        pos = [[2,1],[5,0],[4,3],[7,6]]
        dist = numpy.array([0.1,0.13,0.17,0.21,0.24,0.08,0.09,0.11,0])
        self.assertEqual((dist,pos),readtree(self.tree,otusid))

    def test_partialnotsortedread(self):
        otusid = ['b','e','a']
        pos = [[0,2],[1,3]]
        dist = numpy.array([0.13 + 0.08,0.24 + 0.11,0.1,0.09,0])
        self.assertEqual((dist,pos),readtree(self.tree,otusid))

    def test_notrootedread(self):
        otusid = ['c','b']
        pos = [[0,1]]
        dist = numpy.array([0.17,0.13,0.08 + 0.09])
        self.assertEqual((dist,pos),readtree(self.tree,otusid))

    def test_oneotu(self):
        otusid = ['c']
        pos = []
        dist = numpy.array([0.17 + 0.08 + 0.09])
        self.assertEqual((dist,pos),readtree(self.tree,otusid))

    def test_voidotus(self):
        otusid = []
        self.assertRaises(ValueError, readtree, self.tree,otusid)

if __name__ =='__main__':
    main()
