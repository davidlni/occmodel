#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is code is commercial software.
# Copyright 2007 by Runar Tenfjord, Tenko.
import sys
import unittest

from math import pi

sys.path.insert(0, '..')
from occmodel import Point, Transform

class test_Transform(unittest.TestCase):
    def almostEqual(self, a, b, places = 7):
        for va,vb in zip(a,b):
            self.assertAlmostEqual(va, vb, places)
        
    def test_init_and_accessors(self):
        eq = self.almostEqual
        m = Transform()
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (1.,0.,0.,0.,
             0.,1.,0.,0.,
             0.,0.,1.,0.,
             0.,0.,0.,1.))
        
        m = Transform(*range(1,17))
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            range(1,17))
        
        m = Transform((( 1,  2,  3,  4),
                    ( 5,  6,  7,  8),
                    ( 9, 10, 11, 12),
                    (13, 14, 15, 16)))
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            range(1,17))
        
        m = Transform()
        m[0][0] = 1; m[0][1] = 2; m[0][2] = 3; m[0][3] = 4
        m[1][0] = 5; m[1][1] = 6; m[1][2] = 7; m[1][3] = 8
        m[2][0] = 9; m[2][1] = 10; m[2][2] = 11; m[2][3] = 12
        m[3][0] = 13; m[3][1] = 14; m[3][2] = 15; m[3][3] = 16
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            range(1,17))
        
        m = Transform(*range(1,17))
        n = m[0]
        eq((n[0], n[1], n[2], n[3],),
            range(1,5))
        
        n = m[1]
        eq((n[0], n[1], n[2], n[3],),
            range(5,9))
        
        n = m[2]
        eq((n[0], n[1], n[2], n[3],),
            range(9,13))
        
        n = m[3]
        eq((n[0], n[1], n[2], n[3],),
            range(13,17))
        
        n[0] = 17
        eq((n[0], n[1], n[2], n[3],),
            (17,14,15,16))
            
    def test_translate(self):
        eq = self.almostEqual
        m = Transform().translate(2)
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (1., 0., 0., 2.,
             0., 1., 0., 0.,
             0., 0., 1., 0.,
             0., 0., 0., 1.))
                             
        m = Transform().translate(2,3)
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (1., 0., 0., 2.,
             0., 1., 0., 3.,
             0., 0., 1., 0.,
             0., 0., 0., 1.))
        
        m = Transform().translate(2,3,4)
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (1., 0., 0., 2.,
             0., 1., 0., 3.,
             0., 0., 1., 4.,
             0., 0., 0., 1.))
        
        m = Transform().translate((2,3,4))
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (1., 0., 0., 2.,
             0., 1., 0., 3.,
             0., 0., 1., 4.,
             0., 0., 0., 1.))
        
    def test_scale(self):
        eq = self.almostEqual
        m = Transform().scale(2)
        
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (2., 0., 0., 0.,
             0., 1., 0., 0.,
             0., 0., 1., 0.,
             0., 0., 0., 1.))
        
        m = Transform().scale(2,3)
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (2., 0., 0., 0.,
             0., 3., 0., 0.,
             0., 0., 1., 0.,
             0., 0., 0., 1.))
        
        m = Transform().scale(2,3,4)
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (2., 0., 0., 0.,
             0., 3., 0., 0.,
             0., 0., 4., 0.,
             0., 0., 0., 1.))
        
        m = Transform().scale((2,3,4))
        eq((m[0][0], m[0][1], m[0][2], m[0][3],
            m[1][0], m[1][1], m[1][2], m[1][3],
            m[2][0], m[2][1], m[2][2], m[2][3],
            m[3][0], m[3][1], m[3][2], m[3][3]),
            (2., 0., 0., 0.,
             0., 3., 0., 0.,
             0., 0., 4., 0.,
             0., 0., 0., 1.))
    
    def test_rotate(self):
        eq = self.almostEqual
        m = Transform().rotateZ(pi/2.)
        eq(m.map((1.,0.)), (0.,1.))
        
    def test_map(self):
        eq = self.almostEqual
        p = Point(1,2,3)
        m = Transform().translate((2,3,4))
        eq(m.map(p), (3,5,7))
        
        p = Point(1,2,3)
        m = Transform().scale((2,2,2))
        eq(m.map(p), (2,4,6))
        
        p = ((1,2,3), (3,2,1))
        m = Transform().scale((2,2,2))
        res = m.map(p)
        eq((res[0][0], res[0][1], res[0][2],
            res[1][0], res[1][1], res[1][2],),
            (2.0, 4.0, 6.0,
             6.0, 4.0, 2.0))
             
        p = (Point(1,2,3), Point(3,2,1))
        m = Transform().scale((2,2,2))
        res = m.map(p)
        eq((res[0][0], res[0][1], res[0][2],
            res[1][0], res[1][1], res[1][2],),
            (2.0, 4.0, 6.0,
             6.0, 4.0, 2.0))
             
if __name__ == "__main__":
    sys.dont_write_bytecode = True
    unittest.main()