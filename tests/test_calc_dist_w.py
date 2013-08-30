#!/usr/bin/env python

import numpy
from cogent.util.unit_test import TestCase, main
from sparse_unifrac.unifraccsmat import calc_dist_weighted

class CalcDistWeightedTests(TestCase):

    def setUp(self):
        self.vec1 = numpy.array([5,0,3,2,1,0])
        self.vec3 = numpy.array([6,7,0,1,3,2])
        self.dist = numpy.array([0.1,0.13,0.17,0.21,0.24,0.03])
        
    def test_equal(self):
        sol = 0.0
        s1 = sum(self.vec1)
        self.assertEqual(sol,calc_dist_weighted(self.vec1,self.vec1,self.dist,s1,s1))

    def test_dist(self):
        s1 = sum(self.vec1)
        s3 = sum(self.vec3)
        sol = (5./11 - 6./19)*0.1 + (7./19)*0.13 + (3./11)*0.17 + (2./11 - 1./19)*0.21 + (3./19 - 1./11)*0.24 + (2./19)*0.03
        self.assertEqual(sol,calc_dist_weighted(self.vec1,self.vec3,self.dist,s1,s3))

if __name__ =='__main__':
    main()
