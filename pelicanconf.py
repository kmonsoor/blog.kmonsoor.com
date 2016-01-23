#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#  TODO Cleanup needed

# Site settings.
AUTHOR = u'Khaled Monsoor'
AUTHOR_EMAIL = u'k@kmonsoor.com'
SITENAME = u'KMonsoor\'s Blog'
# TAGLINE = 'my writing corner ...'

# SITEURL = 'https://blog.kmonsoor.com'
SITEURL = ''
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
GOOGLE_DRIVE_ROOT = 'https://googledrive.com/host/0B_IybRcQsDwaTGduUi1jR3h6aDQ/blog/'

TIMEZONE = 'Asia/Dhaka'

DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True

LINKS_WIDGET_NAME = "Professional profiles"
LINKS = (
    ('PDF resume', GOOGLE_DRIVE_ROOT + 'Resume__KhaledMonsoor.pdf'),
    ('Careers 2.0', 'http://careers.stackoverflow.com/kmonsoor'),
    ('LinkedIn', 'http://linkedin.com/in/kmonsoor'),
    ('Github', 'http://github.com/kmonsoor'),
)


# Social widget.
SOCIAL_WIDGET_NAME = "Social"
SOCIAL = (
    ('@KhaledMonsoor', 'http://twitter.com/KhaledMonsoor'),
    ('+KhaledMonsoor', 'http://plus.google.com/+KhaledMonsoor?rel=author'),
    # ('Instagram', 'http://www.instagram.com/kmonsoor/'), 
)

TWITTER_USERNAME = 'KhaledMonsoor'
GITHUB_URL = 'https://github.com/kmonsoor/'
DISQUS_SITENAME = 'kmonsoor'

# Analytics
GOOGLE_ANALYTICS = 'UA-20431143-1'
GOOGLE_ANALYTICS_PROPERTY = 'auto'


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


# Feed
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None


# Theme
THEME = 'plumage'

DEFAULT_PAGINATION = 20
#COPYRIGHT =  'All contents are under The MIT License (MIT).'
DISCLAIMER = 'All opinions expressed in this site are my own personal opinions \
              and are not endorsed by, nor do they represent the opinions of my \
              previous, current and future employers or any of its affiliates, \
              partners or customers.'

# Plugin
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gzip_cache',
           'assets', 
           'sitemap', 
           'pelican_youtube',
           # 'related_posts',
           'tipue_search',
           # 'neighbors',
           'pelican_gist',
           # 'optimize_images',  # generates error while optimizing JPG
           # Core plugins
           # 'thumbnailer',
]


# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
#FILENAME_METADATA = '(?P<slug>.*)'

### Plugin-specific settings
# RELATED_POSTS_MAX = 5
# SITESUBTITLE = "my internet corner"


# for highlighting code-segments
# PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}
MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=native)',
                 # 'mdx_video',
                 'extra',
                 ]

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'search']

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

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


TAG_FEED_RSS = 'tag/%s/feed/index.html'
TAG_FEED_ATOM = 'tag/%s/feed/atom/index.html'
CATEGORY_FEED_RSS = 'category/%s/feed/index.html'
CATEGORY_FEED_ATOM = 'category/%s/feed/atom/index.html'

FEED_MAX_ITEMS = 10
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Tech'
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = True


# Sitemap.
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

### Theme-specific settings
IMAGE_PATH = "images/"
THUMBNAIL_DIR = "images/"
SITE_THUMBNAIL = "/logo.png"
# THUMBNAIL_SIZES = {'thumbnail': '462x?',}
DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}">
<img src="{thumbnail}" alt="{filename}"></a>"""



MENUITEMS = (
     ('Home', '/'),
     ('Tech', '/category/tech/'),
#     ('About', '/about/'),
)


TIPUE_SEARCH = True
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True
