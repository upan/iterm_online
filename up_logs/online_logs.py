#!/usr/bin/env python

import logging
import term_logs
import write_logs



def Terminal_info(parater):
  term_logs.terminal_info(parater)
def Terminal_warning(parater):
  term_logs.terminal_warning(parater)
def Terminal_error(parater):
  term_logs.terminal_error(parater)



def Logs_info(parater):
  write_logs.logs_info(parater)
def Logs_warging(parater):
  write_logs.logs_warning(parater)
def Logs_error(parater):
  write_logs.logs_error(parater)




def Logs_info_all(parater):
  Terminal_info(parater)
  Logs_info(parater)
def Logs_warning_all(parater):
  Terminal_warning(parater)
  Logs_warning(parater)
def Logs_error_all(parater):
  Terminal_error(parater)
  Logs_error(parater)
