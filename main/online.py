#!/usr/bin/env python
#coding:utf-8
import optparse
import sys
import global_setting
from download import down_git
from env import env_test,env_online
import rsync_salt
from mail import send_mail
import term_init
#from up_logs import new_logs

#logs = new_logs.Loggger('../logs/test_online.log')



parse=optparse.OptionParser(usage='"usage:%prog -n iterm_name -a test|online|test_b|online_b"',version="%prog 1.0")
parse.add_option('-n',dest='name',action='store',type=str,metavar='iter_name',help='Enter Your iterm Name!!')
parse.add_option('-a',dest='action',action='store',type=str,metavar='iterm_action',help='Enter Your action  "test|gray|online|test_b|gray_b|online_b" for iterm')
(options,args)=parse.parse_args()

iterm_name = options.name
iterm_action = options.action



#print len(sys.argv)



def test_online(iterm):
  #下载git项目
  term_init.term_check(iterm)
  down_git.iterm_down(iterm)
  #创建项目并生成项目版本
  env_test.file_create_online_test(iterm)
  env_online.file_create_online(iterm)
  #通过salt结合rsync同步版本到测试环境中
  rsync_salt.To_online(iterm,'test')
  send_mail.term_mail(iterm,'test')

def test_back(iterm):
  #回退版本至上一版本
  env_test.Rollback_test(iterm)
  env_online.Rollback(iterm)
  #通过salt结合rsync同步版本到测试环境中
  rsync_salt.To_online(iterm,'test')
  send_mail.term_mail(iterm,'test_b')
  
def gray_online(iterm):
  #通过salt结合rsync同步版本到测试环境中
  rsync_salt.To_online(iterm,'gray')
  send_mail.term_mail(iterm,'gray')

def gray_back(iterm):
  #回退版本至上一版本
  env_online.Rollback(iterm)
  env_test.Rollback_test(iterm)
  #通过salt结合rsync同步版本到测试环境中
  rsync_salt.To_online(iterm,'test')
  rsync_salt.To_online(iterm,'gray')
  send_mail.term_mail(iterm,'gray_b')

def online(iterm):
  #通过salt结合rsync同步版本到测试环境中
  rsync_salt.To_online(iterm,'online')
  send_mail.term_mail(iterm,'online')

def online_back(iterm):
  #回退版本至上一版本
  env_online.Rollback(iterm)
  env_test.Rollback_test(iterm)
  #通过salt结合rsync同步版本到测试环境中
  rsync_salt.To_online(iterm,'test')
  rsync_salt.To_online(iterm,'gray')
  rsync_salt.To_online(iterm,'online')
  send_mail.term_mail(iterm,'online_b')

#test_online('abc')
#test_back('abc')
#gray_online('abc')
#gray_back('abc')
#online('abc')
#online_back('abc')


if len(sys.argv) != 5 or sys.argv[1] != '-n' or sys.argv[3] != '-a':
  print '\033[31;1mPlease input again,参数有误\033[0m"'
  print '\033[33;1mUsage: "usage:online.py -n iterm_name -a test|online|test_b|online_b\033[0m"'
  sys.exit()

if iterm_action == "test":
  test_online(iterm_name)
elif iterm_action == "gray":
  gray_online(iterm_name)
elif iterm_action == "online":
  online(iterm_name)
elif iterm_action == "test_b":
  test_back(iterm_name)
elif iterm_action == "gray_b":
  gray_back(iterm_name)
elif iterm_action == "online_b":
  online_back(iterm_name)
else:
  print '\033[31;1mPlease input again,参数有误\033[0m"'
  print '\033[33;1mUsage: "usage:online.py -n iterm_name -a test|online|test_b|online_b\033[0m"'
  #usage:%prog -h
  sys.exit()
  


