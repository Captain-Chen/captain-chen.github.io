# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir) # Add to PATH environment
from pelicanconf import * # Import the pelicanconf.py as a module

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://captain-chen.github.io'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""