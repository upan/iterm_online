#! /usr/bin/env python
#coding=utf-8

import logging,os

class Loggger:
#def __init__(self, path):
# self.logger_logs = logging.getLogger('mylog2')
# self.logger_ter = logging.getLogger('liyuanchuan')
# self.logger_logs.setLevel(logging.DEBUG)
# self.logger_ter.setLevel(logging.DEBUG)
# fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
# fmt2 = logging.Formatter('%(levelname)s - %(message)s')
# self.sh = logging.StreamHandler()
# self.sh.setFormatter(fmt2)
# self.sh.setLevel(logging.INFO)
# self.fh = logging.FileHandler(path)
# self.fh.setFormatter(fmt)
# self.fh.setLevel(logging.DEBUG)
# self.logger_ter.addHandler(self.sh)
# self.logger_logs.addHandler(self.fh)
 def first(self):
  self.logger_logs = logging.getLogger('mylog2')
  self.logger_ter = logging.getLogger('liyuanchuan')
  self.logger_logs.setLevel(logging.DEBUG)
  self.logger_ter.setLevel(logging.DEBUG)
  fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
  fmt2 = logging.Formatter('%(levelname)s - %(message)s')
  self.sh = logging.StreamHandler()
  self.sh.setFormatter(fmt2)
  self.sh.setLevel(logging.INFO)
  self.fh = logging.FileHandler("../logs/test_online.log")
  self.fh.setFormatter(fmt)
  self.fh.setLevel(logging.DEBUG)
  self.logger_ter.addHandler(self.sh)
  self.logger_logs.addHandler(self.fh)
 
 def debug_t(self,message):
  self.first()
  self.logger_ter.debug('\033[32;1m %s\033[0m' % message)
  self.logger_ter.removeHandler(self.sh)
  self.logger_logs.removeHandler(self.fh)
  #self.logger_ter.debug(message)

 def info_t(self,message):
  self.first()
  self.logger_ter.info('\033[32;1m %s\033[0m' % message)
  self.logger_ter.removeHandler(self.sh)
  self.logger_logs.removeHandler(self.fh)

 def war_t(self,message):
  self.first()
  self.logger_ter.warn('\033[33;1m %s\033[0m' % message)
  self.logger_ter.removeHandler(self.sh)
  self.logger_logs.removeHandler(self.fh)
  
 def error_t(self,message):
  self.first()
  self.logger_ter.error('\033[31;1m %s\033[0m' % message)
  self.logger_ter.removeHandler(self.sh)
  self.logger_logs.removeHandler(self.fh)

 def cri_t(self,message):
  self.first()
  self.logger_ter.critical('\033[31;1m %s\033[0m' % message)
  self.logger_ter.removeHandler(self.sh)
  self.logger_logs.removeHandler(self.fh)

 def debug(self,message):
  self.first()
  self.logger_logs.debug(message)
  self.logger_logs.removeHandler(self.fh)
  self.logger_ter.removeHandler(self.sh)

 def info(self,message):
  self.first()
  self.logger_logs.info(message)
  self.logger_logs.removeHandler(self.fh)
  self.logger_ter.removeHandler(self.sh)

 def war(self,message):
  self.first()
  self.logger_logs.warn(message)
  self.logger_logs.removeHandler(self.fh)
  self.logger_ter.removeHandler(self.sh)

 def error(self,message):
  self.first()
  self.logger_logs.error(message)
  self.logger_logs.removeHandler(self.fh)
  self.logger_ter.removeHandler(self.sh)

 def cri(self,message):
  self.first()
  self.logger_logs.critical(message)
  self.logger_logs.addHandler(self.fh)
  self.logger_ter.removeHandler(self.sh)

 def debug_all(self,message):
  self.debug(message)
  self.debug_t(message)
 
 def info_all(self,message):
  self.info(message)
  self.info_t(message)

 def war_all(self,message):
  self.war(message)
  self.war_t(message)

 def error_all(self,message):
  self.error(message)
  self.error_t(message)

 def cri_all(self,message):
  self.cri(message)
  self.cri_t(message)
 


#def main():
#  logs = Loggger('../logs/test_online.log')
#  return logs
  
#r_logs().info_t('nihao')
if __name__ == '__main__':
  logs = Loggger()
  logs2 = Loggger()
  logs3 = Loggger()
  logs.war_all('111')
  logs2.war_all('222')
  logs3.war_all('333')
