#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""
author:  Khaled Monsoor <oss@kmonsoor.com>
modified: 19-Nov-2021
license: The MIT License
"""

import sys
from datetime import datetime

MD_TEMPLATE = """
Title: {title}
Date:  {year}-{month}-{day} {hour}:{minute}
Modified:  {year}-{month}-{day} {hour}:{minute}
Category:  
Tags: 
Slug: {slug}
status: draft
Summary: 



"""


def make_entry(title):
    now = datetime.now()
    slug = title.lower().strip().replace(' ', '-')

    new_file = "content/articles/{}{:0>2}{:0>2}_{}.md".format(now.year,
                                                              now.month,
                                                              now.day, slug)
    template = MD_TEMPLATE.strip().format(title=title,
                                          year=now.year, month=now.month, day=now.day,
                                          hour=now.hour, minute=now.minute,
                                          slug=slug)
    with open(new_file, 'w') as f:
        f.write(template)
    print("New post file created at: " + new_file)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print("No title given")
