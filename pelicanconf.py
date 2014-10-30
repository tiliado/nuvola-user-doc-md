# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Import common configuration
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from common_conf import *
sys.path.pop(0)

AUTHOR = 'Tiliado'
SITEURL = ''

PATH = 'content'
PATH_METADATA = r'(?P<type>\w+)/(?P<dirname>.*?/|)?(?P<basename>.*?).md'

PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = False
PAGE_URL = '{dirname}{basename}.html'
PAGE_SAVE_AS = '{dirname}{basename}.html'

ARTICLE_PATHS = ['articles']

OUTPUT_PATH = './output/html'
CACHE_PATH = './output/cache'

TIMEZONE = 'UTC'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M %z'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

RELATIVE_URLS = True
STATIC_PATHS = ['images']

INTERLINKS["apiref"] = "./api_reference.html#"

import re
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

class MarkdownConfigExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.safeMode = False
        md.enable_attributes = False
        md.lazy_ol = False

class LowerHeaderLevelExtension(Extension):
    def __init__(self, step=1, *args, **kwds):
        Extension.__init__(self, *args, **kwds)
        self.step = step
    
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add('lowerheaderlevel', LowerHeaderLevelProcessor(self.step), '_end')
        
class LowerHeaderLevelProcessor(Treeprocessor):
    def __init__(self, step):
        Treeprocessor.__init__(self)
        self.step = step
        self.expr = re.compile('h(\d)')
    
    def run(self, node):
        for child in node.getiterator():
            match = self.expr.match(child.tag)
            if match:
                child.tag = 'h{}'.format(min(6, int(match.group(1)) + self.step))
        return node

MD_EXTENSIONS = [
    MarkdownConfigExtension(), LowerHeaderLevelExtension(),
    'extra', 'toc', 'sane_lists', 'fenced_code', 'codehilite',
    'def_list', 'attr_list', 'abbr', 'admonition'
    ]

def section_filter(path, section, basepath="", label=None):
    for part in (path if not path.endswith(".html") else path[:-5]).split("/"):
        if part == section:
            css_class = ' class="active"'
            break
    else:
        css_class = ""
    
    return '<li{}><a href="{}/{}.html">{}</a></li>'.format(css_class, basepath, section, label or section)
    
JINJA_FILTERS = {"section": section_filter}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ("extract_toc", "bootstrap_admonition", "interlinks")

