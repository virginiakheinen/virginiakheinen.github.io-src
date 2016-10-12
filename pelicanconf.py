#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Virginia K. Heinen'
SITENAME = 'Virginia K. Heinen'
SITEURL = ''

USE_FOLDER_AS_CATEGORY = True 

PATH = 'content'
ARTICLE_PATHS = ['articles',]
PAGE_PATHS = ['pages',]

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = False

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = ()

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = False

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False

# Display the search form
DISPLAY_SEARCH_FORM = False

# Sort pages list by a given attribute
# PAGES_SORT_ATTRIBUTE (Title)

# Display the "Fork me on Github" banner
GITHUB_URL = None


# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

THEME='pelican-blueidea'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
