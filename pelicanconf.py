AUTHOR = 'Richard Nguyen'
BIO_TEXT = 'Independent Developer from Winnipeg, MB'
SITENAME = 'Refactoring Richard'
SITEURL = ''

TIMEZONE = 'Canada/Central'
DEFAULT_LANG = 'En'
THEME = 'themes/mytheme/'

PATH = 'content'
AUTHOR_SAVE_AS = ''
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = 'pages/{slug}'
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
GITHUB_URL = "https://www.github.com/captain-chen"

DIRECT_TEMPLATES = ['index', 'archives'] # what templates to copy over  
DELETE_OUTPUT_DIRECTORY = True # Set to false to retain while debugging

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'}
    }
}

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True