#!/usr/bin/env python3

from setuptools import setup
setup(name='duolingo-save-streak',
      version='0.1',
      description='Saves Duo Streak by buying as much is possible',
      author='Alex Joseph',
      author_email='alexsanjoseph@gmail.com',
      packages=['duolingo-save-streak'],
      package_dir={'duolingo-save-streak': 'bin'},
      install_requires=[
      'duolingo-api',
      ],
     )
