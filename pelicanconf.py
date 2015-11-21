#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site settings.
AUTHOR = u'Khaled Monsoor'
AUTHOR_EMAIL = u'k@kmonsoor.com'
SITENAME = u'kmonsoor\'s online hub'
TAGLINE = 'my little corner on internet ...'
SITEURL = ''
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

TIMEZONE = 'Asia/Dhaka'

DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (('asda', 'http://blog.kmonsoor.com'),)

# Social widget.
SOCIAL = (
    ('Plus', 'http://plus.google.com/+KhaledMonsoor?rel=author'),
    ('Twitter', 'http://twitter.com/KhaledMonsoor'),
    ('Github', 'http://github.com/kmonsoor'),
    ('LinkedIn', 'http://www.linkedin.com/in/kmonsoor'),
    ('Instagram', 'http://www.instagram.com/kmonsoor/'), 
)
TWITTER_USERNAME = 'KhaledMonsoor'
GITHUB_URL = 'https://github.com/kmonsoor/'
DISQUS_SITENAME = 'kmonsoor'
GOOGLE_ANALYTICS = 'UA-20431143-1'
MENUITEMS = ()

# SUMMARY_MAX_LENGTH = 500
# LOAD_CONTENT_CACHE = True

# Content path.
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
    'files/github/.nojekyll': {'path': '.nojekyll'},
    'files/github/CNAME': {'path': 'CNAME'},
    'files/github/404.html': {'path': '404.html'},
    'files/github/README.md': {'path': 'README.md'},
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
}

# URL settings
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
    )   
ARTICLE_URL = ('{slug}/')
ARTICLE_SAVE_AS = ('{slug}/index.html')
PAGE_URL = ('{slug}/')
PAGE_SAVE_AS = ('{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')
# AUTHOR_SAVE_AS = False

# Feed.
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Theme.
THEME = 'razius'
COVER_IMG_URL = '/images/cover.jpg'
COVER_BG_COLOR = '#375152'
TYPOGRIFY = True
DEFAULT_PAGINATION = 5

# Plugin.
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gzip_cache',
           'assets', 
           'optimize_images', 
           'sitemap', 
           'pelican_youtube'
         ]

# for highlighting code-segments
# PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}
MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=native)', 'extra']

# Sitemap.
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'pages': 0.9,
        'indexes': 0.8,
    },
    'changefreqs': {
        'indexes': 'daily',
        'articles': 'daily',
        'pages': 'weekly'
    }
}

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False
