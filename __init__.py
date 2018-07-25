#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2017, Osman Yucel <mail at osmanyucel.com>'

from calibre.customize import EditBookToolPlugin


class PostProcessor(EditBookToolPlugin):

    name = 'PostProcessor For PDF2EPUB'
    version = (1, 0, 0)
    author = 'Osman Yucel'
    supported_platforms = ['windows', 'osx', 'linux']
    description = 'This tool provides a pseudo-smart method to help with manual fixing of Pdf to EPub conversion'
    minimum_calibre_version = (1, 46, 0)
