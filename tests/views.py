# coding=utf8

import unittest

from paste.fixture import TestApp
from nose.tools import assert_equal

import kuku

class TestAdmin():

    def setUp(self):
        middleware = []
        self.app = TestApp(kuku.app.wsgifunc(*middleware))

    def test_index(self):
        response = self.app.get('/')
        assert_equal(response.status, 200)

    def test(self):
        assert True
