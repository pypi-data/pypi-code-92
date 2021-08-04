#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['swapdf']

package_data = \
{'': ['*'], 'swapdf': ['docs/*']}

entry_points = \
{'console_scripts': ['swapdf = swapdf.__main__:main']}

setup(name='swapdf',
      version='0.9.8',
      description='SWAP PDF pages after scan of a two-sided sheet pack through a one-sided feeder.',
      author='Carlo Alessandro Verre',
      author_email='carlo.alessandro.verre@gmail.com',
      url='https://pypi.org/project/swapdf',
      packages=packages,
      package_data=package_data,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
