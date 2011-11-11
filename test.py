import os

gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
print STATIC_ROOT
print "\n"
print PROJECT_DIR
