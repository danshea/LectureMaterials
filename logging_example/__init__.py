# Author: Dan Shea
# Date: 2019.12.10
# Description: __init__.py is executed whenever the package is imported
# This means we can implement logging to be pulled in from here when the
# package is imported, but we don't bother setting up logging when we are
# running our tests.

import logging
logging.basicConfig(filename='foo.log', filemode='w', level=logging.DEBUG, \
                    format='%(asctime)s %(levelname)s: %(message)s')

# DEBUG message
logging.debug('The foo module was imported.')

# INFO message
logging.info('The foo module was imported.')

# WARN message
logging.warn('The foo module was imported!')

# ERROR message
logging.error('Ooops. The foo module was imported!')

# CRITICAL message
logging.critical('Agh! The foo module was imported!')
