#!/usr/bin/env python
#coding=utf-8
import global_setting
import ConfigParser
import string,os,sys
import commands
#from  up_logs  import online_logs as logs
#from up_logs import term_logs,write_logs
from up_logs import new_logs 
#logs = new_logs.r_logs()
#import logging

logs = new_logs.Loggger()

class Git_down:
  def __init__(self,iterm):
    self.Iterm = iterm
    self.Path = '../git_download/%s' % iterm
    #global cf 
    self.cf = ConfigParser.ConfigParser()
    self.cf.read("../conf/config.conf")
    self.secs = self.cf.sections()
    self.username = self.cf.get('git','user')
    self.password = self.cf.get('git','pwd')
  def rm_dir(self):
    isExists = os.path.exists(self.Path)
    if isExists:
      logs.info('rm %s' % self.Path)
      os.system('rm -rf %s' % self.Path) 
  def iterm_name(self):
    if self.Iterm in self.secs:
      self.rm_dir()
      iterm_address = self.cf.get(self.Iterm,'git_address')
      url_path_os = "echo " + iterm_address + " | awk -F// '{print $2}'"
      url_path = os.popen(url_path_os).read().strip('\n')
      logs.info_all('get git_address from %s is  %s' % (self.Iterm,iterm_address))
      clone_cmd = 'git clone' + ' http://' + self.username + ':' + self.password + '@' + url_path + ' ' + self.Path
      (status,output) = commands.getstatusoutput(clone_cmd)
      if status == 0:
        logs.info_all('down git_address success')
        return True
      else:
        logs.error_all('config gitaddress  %s is Error ' % iterm_address )
        return False
        sys.exit(1)
    else:
      return False
      sys.exit(1)

def iterm_down(iterm):
  A = Git_down(iterm)
  A.iterm_name()

#A = Git_down('abc')
#A.iterm_name()
