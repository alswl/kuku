# coding=utf-8

import os

DEBUG = True

ADMIN = 'alswl'
PASSWORD = '123456'

ROOT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')
UPLOAD_DIR = os.path.join(ROOT_DIR, 'upload')

DEFAULT_DIR_MODE = '755'
DEFAULT_FILE_MODE = '644'

NOT_ALLOWD_NAME = ['admin']
