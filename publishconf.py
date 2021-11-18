#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.kmonsoor.com'
RELATIVE_URLS = False

ARTICLE_EXCLUDES = ['drafts', ]

# Following items are often useful when publishing


# Analytics
GOOGLE_ANALYTICS = 'G-B3VL9K9558'
COMMENTBOX_PROJECT = '5722781509484544-proj'
PINTEREST_VERIFICATION_ID = '8b5dd0090347e2d6ff8beeb1cb8a2f3e'