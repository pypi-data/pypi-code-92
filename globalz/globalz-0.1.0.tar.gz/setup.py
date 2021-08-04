# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['globalz']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'globalz',
    'version': '0.1.0',
    'description': '"I provide zee globalz\\!" said the library in a thick French accent. "It\'s like Lua\'s _G object, but for Python\\!"',
    'long_description': '# globalz\n\n> "I provide zee globalz\\!" said the library in a thick French accent. "It\'s like Lua\'s _G object, but for Python\\!"\n\nWARNING: This repo is in development. It was automatically generated with [mkpylib](https://github.com/shawwn/scrap/blob/master/mkpylib). If you\'re reading this message, it means that I use this repo for my own purposes right now. It might not do anything at all; the default functionality is `print(\'TODO\')`.\n\nIf you really want to try it out, feel free. I recommend reading through the code and commit history to see if it does what you need, or [ask me](#contact) for status updates.\n\nStay tuned!\n\n## Install\n\n```\npython3 -m pip install -U globalz\n```\n\n## Usage\n\n```py\nimport globalz\n\nprint(\'TODO\')\n```\n\n## License\n\nMIT\n\n## Contact\n\nA library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!\n\nMy Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It\'s the best way to reach me, and I\'m always happy to hear from you.\n\n- Twitter: [@theshawwn](https://twitter.com/theshawwn)\n- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)\n- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)\n- Website: [shawwn.com](https://www.shawwn.com)\n\n',
    'author': 'Shawn Presser',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shawwn/globalz',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
