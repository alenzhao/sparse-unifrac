#!/usr/bin/env python

import numpy
from cogent.util.unit_test import TestCase, main
from sparse_unifrac.unifraccsmat import dev_vec_weighted

class DevVecWeightedTests(TestCase):

    def setUp(self):
        self.vec0 = numpy.array([0,0,0,0])
        self.vec = numpy.array([0,3,2,5])
        self.pos = [[2,3],[4,1],[0,5]]
        
    def test_all0(self):
        dev = numpy.array([0,0,0,0,0,0,0])
        self.assertEqual(dev,dev_vec_weighted(self.pos,self.vec0))

    def test_dev(self):
        dev = numpy.array([0,3,2,5,7,10,10])
        self.assertEqual(dev,dev_vec_weighted(self.pos,self.vec))    

if __name__ =='__main__':
    main()
