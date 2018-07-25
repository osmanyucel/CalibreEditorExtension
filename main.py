#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

import re

from PyQt5.Qt import QAction, QInputDialog
from calibre import force_unicode
from calibre.ebooks.oeb.polish.container import OEB_DOCS, OEB_STYLES, serialize
from calibre.gui2 import error_dialog
from calibre.gui2.tweak_book.plugin import Tool
from cssutils.css import CSSRule

__license__ = 'GPL v3'
__copyright__ = '2017, Osman Yucel <mail at osmanyucel.com>'

class RemovePageNumbers(Tool):

    name = 'RemovePageNumbers'
    allowed_in_toolbar = True
    allowed_in_menu = True

    def create_action(self, for_toolbar=True):
        ac = QAction(get_icons('images/pageNumber.png'), 'Remove Page Numbers', self.gui)
        ac.triggered.connect(self.remove)
        return ac

    def remove(self):
        self.boss.add_savepoint('Before: Removing Page Numbers')
        container = self.current_container
        for name, mt in container.mime_map.iteritems():
            if mt in OEB_DOCS:
                html = container.raw_data(name)
                html = re.sub(r'<p>[0-9]{1,3}</p>', r'', html)
                container.open(name, 'wb').write(html)
                container.dirty(name)
        self.boss.show_current_diff()
        self.boss.apply_container_update_to_gui()
        return self
class RemovePageLinks(Tool):

    name = 'RemovePageLinks'
    allowed_in_toolbar = True
    allowed_in_menu = True

    def create_action(self, for_toolbar=True):
        ac = QAction(get_icons('images/pageNumber.png'), 'Remove Page Links', self.gui)
        ac.triggered.connect(self.remove)
        return ac

    def remove(self):
        self.boss.add_savepoint('Before: Removing Page Links')
        container = self.current_container
        for name, mt in container.mime_map.iteritems():
            if mt in OEB_DOCS:
                html = container.raw_data(name)
                html = re.sub(r'<a id="p[0-9]*"></a>', r'', html)
                container.open(name, 'wb').write(html)
                container.dirty(name)
        self.boss.show_current_diff()
        self.boss.apply_container_update_to_gui()
        return self
class ConnectBrokenParagraphs(Tool):

    name = 'ConnectBrokenParagraphs'
    allowed_in_toolbar = True
    allowed_in_menu = True

    def create_action(self, for_toolbar=True):
        ac = QAction(get_icons('images/connectParagraph.png'), 'Connect Broken Paragraph', self.gui)
        ac.triggered.connect(self.remove)
        return ac

    def remove(self):
        self.boss.add_savepoint('Before: Connecting Paragraph')
        container = self.current_container
        for name, mt in container.mime_map.iteritems():
            if mt in OEB_DOCS:
                html = container.raw_data(name)
                html = re.sub(r'(-</p>[\s]*<p>)([a-zğıüöçş])', r'\2', html)
                html = re.sub(r'([a-zA-Z,])(</p>[\s]*<p>)', r'\1 ', html)
                html = re.sub(r'(</p>[\s]*<p>)([a-zğıüöçş])', r' \2', html)
                html = re.sub(r'([^.?!”"])(</p>[\s]*<p>)', r'\1 ', html)
                container.open(name, 'wb').write(html)
                container.dirty(name)
        self.boss.show_current_diff()
        self.boss.apply_container_update_to_gui()
        return self
class CleanUp(Tool):
    name = 'cleanUp'
    allowed_in_toolbar = True
    allowed_in_menu = True

    def create_action(self, for_toolbar=True):
        ac = QAction(get_icons('images/cleanUp.png'), 'cleanUp', self.gui)
        ac.triggered.connect(self.remove)
        return ac

    def remove(self):
        self.boss.add_savepoint('Before: Cleaning Up')
        container = self.current_container
        for name, mt in container.mime_map.iteritems():
            if mt in OEB_DOCS:
                html = container.raw_data(name)
                html = re.sub(r' class="calibre[0-9]*"', r'', html)
                while '  ' in html:
                    html = html.replace('  ', ' ')
                html = html.replace('> ', '>')
                html = html.replace(' </', '</')
                container.open(name, 'wb').write(html)
                container.dirty(name)
        self.boss.show_current_diff()
        self.boss.apply_container_update_to_gui()
        return self
