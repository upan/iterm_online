#!/usr/bin/env python

import logging

logger_file = logging.getLogger()
fh = logging.FileHandler('../logs/test.log')
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter1)
logger_file.addHandler(fh)
logger_file.setLevel(logging.INFO)
def logs_info(parater):
  logger_file.info('%s' % parater)
def logs_warning(parater):
  logger_file.warning('%s' % parater)
def logs_error(parater):
  logger_file.error('%s' % parater)



