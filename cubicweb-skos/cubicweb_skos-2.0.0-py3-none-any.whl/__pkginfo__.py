# pylint: disable=W0622
"""cubicweb-skos application packaging information"""


modname = 'cubicweb_skos'
distname = 'cubicweb-skos'

numversion = (2, 0, 0)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
author = 'LOGILAB S.A. (Paris, FRANCE)'
author_email = 'contact@logilab.fr'
description = '"SKOS implementation for cubicweb"'
web = 'http://www.cubicweb.org/project/%s' % distname

__depends__ = {
    'cubicweb': '>= 3.26.0',
}
__recommends__ = {
    'rdflib': '>= 4.1',
    'python-librdf': None,
}

classifiers = [
    'Environment :: Web Environment',
    'Framework :: CubicWeb',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: JavaScript',
]
