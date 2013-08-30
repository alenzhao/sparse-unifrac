#!/usr/bin/env python

import numpy
from cogent.util.unit_test import TestCase, main
from unifraccsmat import calc_dist3 as calc_dist

class CalcDistUnweightedTests(TestCase):

    def setUp(self):
        self.vec1 = numpy.array([True,False,True,False,True,True])
        self.vec2 = numpy.array([False,True,False,True,False,False])
        self.vec3 = numpy.array([True,True,False,False,False,True])
        self.dist = numpy.array([0.1,0.13,0.17,0.21,0.24,0.03])
        
    def test_equal(self):
        sol = 0.0
        self.assertEqual(sol,calc_dist(self.vec1,self.vec1,self.dist))

    def test_different(self):
        sol = 1.0
        self.assertEqual(sol,calc_dist(self.vec1,self.vec2,self.dist))

    def test_dist(self):
        sol = (0.13 + 0.17 + 0.24) / (0.1 + 0.13 + 0.17 + 0.24 + 0.03)
        self.assertEqual(sol,calc_dist(self.vec1,self.vec3,self.dist))

if __name__ =='__main__':
    main()
