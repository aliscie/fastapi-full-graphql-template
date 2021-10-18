import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)


APPS = [
    'Users',
    'Chat',
    'posts',
]