#!/usr/bin/env python

import ConfigParser
import global_setting
from up_logs import new_logs
import sys,os
from  salt_api import salt

logs = new_logs.Loggger()

cf = ConfigParser.ConfigParser()
cf.read("../conf/config.conf")
path = os.getcwd()
parent_path = os.path.dirname(path)


def opt(iterm):
  option = cf.options(iterm)
  if 'name' in option and 'git_address' in option and 'local1' in option and 'iterm_path' in option and 'test_ip' in option and 'gray_ip'  in option and 'online_ip'  in option and 'mail_address' in option:
    logs.info('check init config.conf %s success' % iterm)
  else:
    logs.error_all('check init config.conf %s faled,Please check your config.conf again!!!' % iterm)
    sys.exit()
  logs.info_all('%s option check success!' % iterm)

def iterm_file(iterm):
  option = cf.options(iterm)
  local_n = [elem for elem in option if 'local' in elem]
  for i in local_n:
    iterm_file = cf.get(iterm,i)
    iterm_name = os.path.basename(iterm_file)
    find_file_t = parent_path + '/replace_file_t/' + iterm + '/' + iterm_name
    find_file_on = parent_path + '/replace_file_on/' + iterm + '/' +iterm_name
    if os.path.exists(find_file_t) and os.path.exists(find_file_on):
      logs.info('check %s file success!!' % iterm)
    else:
      logs.error_all('%s config %s is Not exits' %(iterm,i))
      sys.exit()
  logs.info_all('%s iterm_file check success!'  % iterm)

def iterm_salt_ip(iterm):
  iterm_file_path = cf.get(iterm,'iterm_path')
  iterm_test_ip = cf.get(iterm,'test_ip')
  iterm_gray_ip = cf.get(iterm,'gray_ip')
  iterm_online_ip = cf.get(iterm,'online_ip')
  test = eval(iterm_test_ip)
  gray = eval(iterm_gray_ip)
  online = eval(iterm_online_ip)
  for i in test:
    mkdir_cmd = 'mkdir  -p ' + iterm_file_path 
    salt.SaltApi(i,mkdir_cmd)
  for i in gray:
    mkdir_cmd = 'mkdir  -p ' + iterm_file_path 
    salt.SaltApi(i,mkdir_cmd)
  for i in online:
    mkdir_cmd = 'mkdir  -p ' + iterm_file_path 
    salt.SaltApi(i,mkdir_cmd)
  logs.info_all('%s salt check success!!' % iterm)
  
def term_check(iterm):
  opt(iterm)
  iterm_file(iterm)
  iterm_salt_ip(iterm)
  
if __name__ == '__main__':
  term_check('abc')
