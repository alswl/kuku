# coding=utf-8

import os
import re

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

def secure_name(name):
    safe_name = re.sub(r'\s+', '-', name)
    return safe_name

def secure_check_path(path): # TODO more powerful
    if '..' in path:
        return False
    if len(path) > 0 and path[0] == '/':
        return False
    return True

class NotFoundError(Exception):
    pass

class IllegalValueError(Exception):
    pass
