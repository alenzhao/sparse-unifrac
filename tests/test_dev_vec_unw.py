#!/usr/bin/env python

import numpy
from cogent.util.unit_test import TestCase, main
from sparse_unifrac.unifraccsmat import dev_vec

class DevVecUnweightedTests(TestCase):

    def setUp(self):
        self.vect = numpy.array([True,True,True,True])
        self.vecf = numpy.array([False,False,False,False])
        self.vec = numpy.array([False,True,False,False])
        self.pos = [[2,3],[4,1],[0,5]]
        
    def test_allfalse(self):
        dev = numpy.array([False,False,False,False,False,False,False])
        self.assertEqual(dev,dev_vec(self.pos,self.vecf))

    def test_alltrue(self):
        dev = numpy.array([True,True,True,True,True,True,True])
        self.assertEqual(dev,dev_vec(self.pos,self.vect))

    def test_dev(self):
        dev = numpy.array([False,True,False,False,False,True,True])
        self.assertEqual(dev,dev_vec(self.pos,self.vec))    

if __name__ =='__main__':
    main()
