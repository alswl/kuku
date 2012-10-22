# coding=utf-8

import os

import config

def get_dir_path(*args):
    path = config.UPLOAD_DIR
    for i in args:
        path = os.path.join(path, i)
    if os.path.isdir(path):
        return path
    else:
        raise ValueError

def get_file_path(*args):
    path = config.UPLOAD_DIR
    for i in args:
        path = os.path.join(path, i)
    if os.path.isfile(path):
        return path
    else:
        raise ValueError

def split_url(url):
    args = url.split('/')
    return args
