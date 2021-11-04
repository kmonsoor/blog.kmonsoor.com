#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# Theme
import plumage
THEME = plumage.get_path()

# SITESUBTITLE = "jack of N trades, master of X"
CODE_STYLE = "monokai"
TIPUE_SEARCH = False

# Site settings.
AUTHOR = 'Khaled Monsoor'
AUTHOR_EMAIL = 'k@kmonsoor.com'
SITENAME = 'I think ...'
# TAGLINE = 'khaled monsoor says ...'
SITE_SUMMARY = "Khaled Monsoor here. I usually write about programming, system-design, Islam, life, travel or just personal thoughts ... "

SITEURL = 'https://blog.kmonsoor.com'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
TIMEZONE = 'Asia/Dhaka'
DEFAULT_LANG = u'en'
MARKDOWN = {
    "extension_configs": {
        # https://python-markdown.github.io/extensions/#officially-supported-extensions
        "markdown.extensions.abbr": {},
        # Example of admonition use at:
        # https://github.com/kdeldycke/kevin-deldycke-blog/blob/main/content/posts/python-ultimate-regular-expression-to-catch-html-tags.md
        "markdown.extensions.admonition": {},
        "markdown.extensions.attr_list": {},
        "markdown.extensions.def_list": {},
        "markdown.extensions.footnotes": {},
        "markdown.extensions.md_in_html": {},
        "markdown.extensions.meta": {},
        # Allow numbered lists to not start with 1. Used in following article:
        # https://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
        "markdown.extensions.sane_lists": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.toc": {
            "permalink": True,
        },
        "mdx_video": {},
        # https://facelessuser.github.io/pymdown-extensions/
        "pymdownx.betterem": {},
        "pymdownx.caret": {},
        "pymdownx.emoji": {},
        "pymdownx.keys": {},
        "pymdownx.magiclink": {},
        "pymdownx.smartsymbols": {},
    },
    "output_format": "html5",
}

TYPOGRIFY = True

# Code block renderers.
SUPERFENCES = True
if SUPERFENCES:
    code_config = {
        "pymdownx.highlight": {
            "linenums": True,
            "linenums_style": "pymdownx-inline",
        },
        "pymdownx.superfences": {
            # No need for magic indention-based code blocks: all ours are
            # delimited by fences anyway.
            "disable_indented_code_blocks": True,
        },
    }
else:
    code_config = {
        "markdown.extensions.codehilite": {
            "linenums": True,
            "linenos": "inline",
            "linespans": "coderow",
            "lineanchors": "L",
            "anchorlinenos": True,
            "wrapcode": True,
        },
        "markdown.extensions.fenced_code": {},
    }
MARKDOWN["extension_configs"].update(code_config)


DELETE_OUTPUT_DIRECTORY = True
TWITTER_USERNAME = 'kmonsoor'
GITHUB_URL = 'https://github.com/kmonsoor/'

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
GOOGLE_ANALYTICS = 'UA-20431143-1'
COMMENTBOX_PROJECT = '5722781509484544-proj'
PINTEREST_VERIFICATION_ID = '8b5dd0090347e2d6ff8beeb1cb8a2f3e'
# GOOGLE_ANALYTICS_PROPERTY = 'auto'
# GOOGLE_TAG_MANAGER_ID = 'GTM-M3VHWXC'


# Content paths
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

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
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

DEFAULT_PAGINATION = 7
DEFAULT_ORPHANS = 2

# COPYRIGHT =  'All contents are under The MIT License (MIT).'
DISCLAIMER = 'All opinions expressed in this site are my own personal opinions \
              and are not endorsed by, nor do they represent the opinions of my \
              previous, current and future employers or any of its affiliates, \
              partners or customers.'

# Do not publish articles set in the future
WITH_FUTURE_DATES = False


DIRECT_TEMPLATES = ['index', 'tags',
                    'categories',
                    # 'authors',
                    'archives', 'search']

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = None
DRAFT_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

FEED_RSS = "feed/index.html"
FEED_ATOM = "feed/atom/index.html"
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
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Sitemap.
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.4,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Theme-specific settings
IMAGE_PATH = "images/"
THUMBNAIL_DIR = "images/"
SITE_THUMBNAIL = "/logo.png"
SITE_THUMBNAIL_TEXT = "comes with a beard"


ARTICLE_EDIT_LINK = (
    "https://github.com/kmonsoor/blog.kmonsoor.com/edit/live/content/articles/"
    "%(slug)s.md"
)


MENUITEMS = (
    ('Home', '/'),
    #  ('Tech', '/category/tech/'),
    #  ('Thoughts', '/category/thoughts/')
    #  ('About', '/about/'),
)

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

# Plugins

PLUGINS = [
    "pelican.plugins.seo",
    "pelican.plugins.sitemap",
    "pelican.plugins.similar_posts",
    "pelican.plugins.neighbors",
    "pelican.plugins.webassets"
]

# pelican.plugins.seo
SEO_REPORT = True
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = True


# pelican.plugins.similar_posts
SIMILAR_POSTS_MAX_COUNT = 3
