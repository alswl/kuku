# coding=utf-8

import os

from web.webapi import NotFound

import config

def get_dir_path(*args):
    path = config.UPLOAD_DIR
    for i in args:
        path = os.path.join(path, i)
    if os.path.isdir(path):
        return path
    else:
        NotFound()

def get_file_path(*args):
    path = config.UPLOAD_DIR
    for i in args:
        path = os.path.join(path, i)
    if os.path.isfile(path):
        return path
    else:
        NotFound()

def split_url(url):
    args = url.split('/')
    return args
