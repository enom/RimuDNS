#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = "Abdallah Deeb <abdallah@deeb.me>"
import os
from setuptools import setup
NAME = "rimudns"
GITHUB_URL = "https://github.com/abdallah/%s" % (NAME)
DESCRIPTION = "Python interface to RimuHosting/Zonomi DNS "

VERSION = "0.0.1"


def read(fname):
    full_path = os.path.join(os.path.dirname(__file__), fname)
    if os.path.exists(fname):
        return open(full_path).read()
    else:
        return ""

try:
    from rimudns.consts import VERSION
except ImportError:
    for line in read('rimudns/consts.py').split('\n'):
        if line.startswith('VERSION'):
            VERSION = \
                line.split('=')[1].replace('"', '').replace("'", '').strip()
requirements = ['lxml', 'dnspython']

setup(name=NAME,
      version=VERSION,
      # download_url="%s/zipball/master" % (GITHUB_URL, VERSION),
      download_url="%s/zipball/master" % GITHUB_URL,
      description=DESCRIPTION,
      install_requires=['lxml', 'dnspython'],
      author='Abdallah Deeb',
      author_email='abdallah@deeb.me',
      url=GITHUB_URL,
      long_description=read('README.md'),
      license='GPLv3+',
      zip_safe=False,
      packages=['rimudns'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
        ],
      )
