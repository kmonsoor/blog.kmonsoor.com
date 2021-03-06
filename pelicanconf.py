#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site settings.
AUTHOR = 'Khaled Monsoor'
AUTHOR_EMAIL = 'k@kmonsoor.com'
SITENAME = 'Khaled Monsoor :: Blog'
TAGLINE = 'khaled monsoor says ...'
SITE_SUMMARY = "Khaled Monsoor here. I usually write about programming, system-design, Islam, life, travel or just personal thoughts ... "

SITEURL = 'https://blog.kmonsoor.com'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
TIMEZONE = 'Asia/Dhaka'

DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True

TWITTER_USERNAME = 'kmonsoor'
GITHUB_URL = 'https://github.com/kmonsoor/'
# DISQUS_SITENAME = 'kmonsoor'


LINKS_WIDGET_NAME = "Professional"
LINKS = (
    ('StackOverflow', 'https://stackoverflow.com/users/617185/kmonsoor'),
    ('LinkedIn', 'https://linkedin.com/in/kmonsoor'),
    ('Github', GITHUB_URL),
)

# Social widget.
SOCIAL_WIDGET_NAME = "Social"
SOCIAL = (
    ('Twitter', "https://twitter.com/kmonsoor"),
    # ("Photos", "https://photos.kmonsoor.com"),
)

# Analytics
# GOOGLE_ANALYTICS = 'UA-20431143-1'
# GOOGLE_ANALYTICS_PROPERTY = 'auto'
# GOOGLE_TAG_MANAGER_ID = 'GTM-M3VHWXC'
PINTEREST_VERIFICATION_ID = '8b5dd0090347e2d6ff8beeb1cb8a2f3e'



# Content path.
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
ARTICLE_EXCLUDES = ['drafts']
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
    'files/github/.nojekyll': {'path': '.nojekyll'},
    'files/github/CNAME': {'path': 'CNAME'},
    'files/github/404.html': {'path': '404.html'},
    'files/github/README.md': {'path': 'README.md'},
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    'images/logo.png': {'path': 'logo.png'}
}

# URL settings
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_SAVE_AS = False

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = None

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Feed
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None

# Theme
THEME = 'plumage'

DEFAULT_PAGINATION = 7
DEFAULT_ORPHANS = 2

# COPYRIGHT =  'All contents are under The MIT License (MIT).'
DISCLAIMER = 'All opinions expressed in this site are my own personal opinions \
              and are not endorsed by, nor do they represent the opinions of my \
              previous, current and future employers or any of its affiliates, \
              partners or customers.'

# Plugin
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gzip_cache',
           'sitemap',
           'minify',
           ]

MINIFY = {
    'remove_comments': True,
    'remove_all_empty_space': True,
    'remove_optional_attribute_quotes': False
}

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# for highlighting code-segments
# PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}
# MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=native)',
#                  # 'mdx_video',
#                  'extra',
#                  ]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.toc': {
            # 'permalink': 'true'
            },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
    'lazy_ol': False,  # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
}

DIRECT_TEMPLATES = ['index', 'tags',
                    'categories',
                    # 'authors',
                    'archives', 'search']

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAG_FEED_RSS = 'tag/{slug}/feed/index.html'
TAG_FEED_ATOM = 'tag/{slug}/feed/atom/index.html'
CATEGORY_FEED_RSS = 'category/{slug}/feed/index.html'
CATEGORY_FEED_ATOM = 'category/{slug}/feed/atom/index.html'

FEED_MAX_ITEMS = 10
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Tech'
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = True

# Sitemap.
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.4,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Theme-specific settings
IMAGE_PATH = "images/"
THUMBNAIL_DIR = "images/"
SITE_THUMBNAIL = "/logo.png"
THUMBNAIL_SIZES = {'thumbnail': '462x?', }
DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}">
<img src="{thumbnail}" alt="{filename}"></a>"""

ARTICLE_EDIT_LINK = "https://github.com/kmonsoor/blog.kmonsoor.com/edit/live/content/articles"

MENUITEMS = (
    ('Home', '/'),
    #  ('Tech', '/category/tech/'),
    #  ('Thoughts', '/category/thoughts/')
    #  ('About', '/about/'),
)

TIPUE_SEARCH = False
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

COMMENTBOX_PROJECT = '5722781509484544-proj'
