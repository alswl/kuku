# coding=utf8

import unittest
import time
import json

from paste.fixture import TestApp
from nose.tools import assert_equal, assert_true

import kuku

class TestAdmin():

    BASE_URL = 'http://localhost'

    def login(self):
        response = self.app.post('/_admin/login',
                                 params='username=alswl&password=123456')
        assert_equal(response.status, 303)
        self.cookie = response.header('Set-Cookie')

    def setUp(self):
        #middleware = []
        self.app = TestApp(kuku.application)

    def test_index(self):
        response = self.app.get('/')
        assert_equal(response.status, 303)
        assert_equal(self.BASE_URL + '/_admin/login',
                     response.header('Location'))

    def test_login(self):
        response = self.app.get('/_admin/login')
        assert_equal(response.status, 200)

        response = self.app.post('/_admin/login',
                                 params='username=alswl&password=123456')
        assert_equal(response.status, 303)
        assert_equal(self.BASE_URL + '/', response.header('Location'))

        response = self.app.post('/_admin/login',
                                 params='username=alswl&password=wrong')
        assert_equal(response.status, 303)
        assert_equal(self.BASE_URL + '/_admin/login',
                     response.header('Location'))

        self.login()
        response = self.app.post('/_admin/login',
                                 params='username=alswl&password=123456',
                                 headers={'Cookie': self.cookie})
        assert_equal(response.status, 303)
        assert_equal(self.BASE_URL + '/',
                     response.header('Location'))

    def test_logout(self):
        response = self.app.get('/_admin/logout')
        assert_equal(response.status, 303)
        assert_equal(self.BASE_URL + '/_admin/login',
                     response.header('Location'))
        
        self.login()
        response = self.app.get('/_admin/logout',
                                headers={'Cookie': self.cookie})
        assert_equal(response.status, 303)
        assert_equal(self.BASE_URL + '/',
                     response.header('Location'))

    def test_mkdir_delete(self):
        self.login()
        name = int(time.time())
        response = self.app.post('/_admin/mkdir',
                                 params='path=.&name=%d' %name,
                                 headers={'Cookie': self.cookie})
        assert_equal(response.status, 200)
        assert_equal(json.loads(response.body).get('success'), True)
        response = self.app.post('/_admin/delete',
                                 params='path=.&name=%d' %name,
                                 headers={'Cookie': self.cookie})
        assert_equal(response.status, 200)
        assert_equal(json.loads(response.body).get('success'), True)

    def test_upload(self):
        pass # TODO
