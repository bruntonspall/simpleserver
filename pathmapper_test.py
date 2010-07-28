#!/usr/bin/env python
# encoding: utf-8
"""
pathmapper_test.py

Created by MBS on 2010-07-22.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import unittest
from pathmapper import PathMapper


class pathmapper_test(unittest.TestCase):
    def setUp(self):
        pass

    def testPathMapperCallsFunction(self):
        self.called = False
        def f():
            self.called = True
        p = PathMapper([(r'^/abc$', f)])
        p.resolve('/abc')
        self.assertEquals(True, self.called)

    def testPathMapperCallsFunctionWithArgs(self):
        self.args = ()
        def f(*args):
            self.args = args
        p = PathMapper([(r'^/a/(\w)$', f)])
        p.resolve('/a/b')
        self.assertEquals(('b',), self.args)

    def testPathMapperCallsFunctionWithKWArgs(self):
        self.kwargs = {}
        def f(*args, **kwargs):
            self.kwargs = kwargs
        p = PathMapper([(r'^/a/(?P<key>\w)$', f)])
        p.resolve('/a/b')
        self.assertEquals('b', self.kwargs['key'])

    def testPathMapperReturnsFunctionResult(self):
        def f(*args, **kwargs):
            return True
        p = PathMapper([(r'^/a/(?P<key>\w)$', f)])
        self.assertEquals(True, p.resolve('/a/b'))

    def testPathMapperReturnsNoneOnMissedPath(self):
        p = PathMapper([(r'^/a/(?P<key>\w)$', None)])
        self.assertEquals(None, p.resolve('/b/asc'))
        self.assertEquals(None, p.resolve('/a/bc'))
        self.assertEquals(None, p.resolve('/'))

    def testPathMapperHandlesBothCountAndKeywords(self):
        self.flag = False
        def f(count, key=None):
            if count == '1' and key == 'test':
                self.flag = True
            else:
                print "'%d' '%d'" % (count, key)

        p = PathMapper([(r'^/a/(\d+)/(?P<key>\w+)$', f)])
        p.resolve('/a/1/test')

        self.assertEquals(True, self.flag)



    
if __name__ == '__main__':
    unittest.main()