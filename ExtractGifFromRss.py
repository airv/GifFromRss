#!/usr/bin/python
# coding: utf-8
from __future__ import unicode_literals

import feedparser


d = feedparser.parse('http://helloprocanvas.ldblog.jp/atom.xml')
print(d.feed.title.encode('utf8'))
print("last title")
print(d.entries[0].title)
