# coding=utf-8

import os

DEBUG = True

ADMIN = 'alswl'
PASSWORD = '123456'

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.abspath(os.path.join(ROOT_PATH, 'templates'))
UPLOAD_PATH = os.path.abspath(os.path.join(ROOT_PATH, '..', 'upload'))

MAX_FILE_SIZE = 5 * 1024 * 1024  # 3 * 1024 * 1024 bytes
ALLOWED_EXTENSIONS = ['jpg', 'png', 'gif', 'zip', 'rar', 'gz']

#DEFAULT_DIR_MODE = '755'
#DEFAULT_FILE_MODE = '644'

#NOT_ALLOWD_NAME = ['admin']

