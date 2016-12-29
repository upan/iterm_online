#!/usr/bin/env python

import logging

logger_term = logging.getLogger()
ch = logging.StreamHandler()
formatter2 = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter2)
logger_term.addHandler(ch)
logger_term.setLevel(logging.INFO)
def logs_info(self):
  logger_term.info('\033[32;1m %s\033[0m' % self)
def logs_warning(self):
  logger_term.warning('\033[33;1m%s\033[0m' % self)
def logs_error(self):
  logger_term.error('\033[31;1m%s\033[0m' % self)

