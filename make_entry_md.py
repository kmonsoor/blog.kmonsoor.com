import sys
from datetime import datetime


TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Modified:
Category:
Tags: 
Slug: {slug}
status: draft
Summary: 



"""


def make_entry(title):
    now = datetime.now()
    slug = title.lower().strip().replace(' ', '-')
    
    f_create = "content/articles/{}{:0>2}{:0>2}_{}.md".format(now.year, 
                                                                now.month, 
                                                                now.day, slug)
    template = TEMPLATE.strip().format(title=title,
                                year=now.year, month=now.month, day=now.day, 
                                hour=now.hour, minute=now.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(template)
    print("File created -> " + f_create)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print "No title given"
