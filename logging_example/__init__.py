# Author: Dan Shea
# Date: 2019.12.10
# Description: __init__.py is executed whenever the package is imported
# This means we can implement logging to be pulled in from here when the
# package is imported, but we don't bother setting up logging when we are
# running our tests.

import logging
logging.basicConfig(filename='foo.log', level=logging.DEBUG)
logging.info('foo was imported.')
