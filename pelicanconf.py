#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ysjin'
SITENAME = "ysjin's blog"
# SITEURL = 'http://ysjin.github.io'
# SITETITLE = 'ysjin\'s blog'

COPYRIGHT_YEAR = 2016

# EXTRA_PATH_METADATA = {
#    'extra/custom.css': {'path': 'static/custom.css'},
#    }
# CUSTOM_CSS = 'static/custom.css'


PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

THEME = "/home/jiny/pelicansite/theme-flex"

PLUGIN_PATHS = 'pelican-plugins'
PLUGINS = ['better_codeblock_line_numbering', 'render_math']

MD_EXTENSIONS = [
    'fenced_code',
    'codehilite(css_class=highlight, pygments_style=monokai)',
    'extra']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True


# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/ysjin'),
          ('facebook', 'http://facebook.com/yongseok.jin'),)

MENUITEMS = (('Archive', '/archives.html'),
             ('Category', '/categories.html'),
             ('Tag', '/tags.html'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
