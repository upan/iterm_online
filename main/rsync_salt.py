#!/usr/bin/env python
#coding:utf-8 
import global_setting
from up_logs import new_logs
import string,os,sys
import ConfigParser
import commands
from salt_api import salt
import re

logs = new_logs.Loggger()


path = os.getcwd()
parent_path = os.path.dirname(path)


###生成rsync的配置文件
def To_rsync():
  #生成rsync的配置文件
  cf = ConfigParser.ConfigParser()
  cf.read("../conf/config.conf")
  s = cf.sections()
  To_iterm_file_t = parent_path + "/Iterm/iterm_t/" 
  To_iterm_file_on = parent_path + "/Iterm/iterm_on/"
  cp_cmd_r = 'cp ../conf/rsyncd_tmp.conf ../conf/rsyncd_tmp2.conf'
  logs.info('create rsyncd.conf')
  os.system(cp_cmd_r)
  output = open('../conf/rsyncd_tmp2.conf','a')
  for i in s:
    if i not in 'git':
      output.write("[%s_t]\n" % i)
      output.write("path = %s%s \n\n" %(To_iterm_file_t,i))
      output.write("[%s_on]\n" % i)
      output.write("path = %s%s \n\n" %(To_iterm_file_on,i))
  output.close()
  #移动生成的配置文件到/etc/rsyncd.conf
  cp_cmd_to_r = 'mv ../conf/rsyncd_tmp2.conf /etc/rsyncd.conf'
  logs.info('move new rsyncd to /etc/rsyncd.conf')
  os.system(cp_cmd_to_r)
  
##同步代码到测试服务器
def To_online(iterm,parater):
  #生成rsync配置
  To_rsync()
  #读取test|gray|online的ip
  cf = ConfigParser.ConfigParser()
  cf.read("../conf/config.conf")
  option = cf.options(iterm)
  To_ip = '%s_ip' % parater
  data_config = [elem for elem in option if To_ip in elem]
  if data_config == []:
    logs.error_all('In config.conf %s %s is not exits,Please checkout!!' % (iterm,To_ip)) 
  else:
    iterm_test_ip = cf.get(iterm,To_ip)
    logs.info('get ip from config')
  #读取项目的同步代码的路径
  data_config_path = [elem for elem in option if 'iterm_path' in elem]
  if data_config_path == []:
    logs.error_all('In config.conf %s iterm_path is not exits,Please checkout!!' % iterm)
  else:
    iterm_path = cf.get(iterm,'iterm_path')
    logs.info('get ip iterm_path config')
  if parater == 'test':
    rsync_name = '%s_t' % iterm
  else:
    rsync_name = '%s_on' % iterm
  #执行客户端的rsync的命令，同步代码
  rsync_cmd = "rsync -azp  --delete-after --timeout=15 --contimeout=15  root@192.168.2.204::%s %s/%s --password-file=/tmp/rsync.secret"  %(rsync_name,iterm_path,iterm)
  A = eval(iterm_test_ip)
  for i in A:
    salt.SaltApi(i,rsync_cmd)
    cf = ConfigParser.ConfigParser()
    cf.read("../conf/config.conf")
    option = cf.options(iterm)
    action_term = [elem for elem in option if 'action' in elem]
    if action_term != []:
      for action_t in action_term:
        iterm_file = cf.get(iterm,action_t)
        A = eval(iterm_file)
        for action_t2 in A:
          salt.SaltApi(i,action_t2)
          logs.info('exute %s success' % iterm_file)

if __name__ == '__main__':
  To_online('abc','test')
##To_online('abc','gray')
#To_rsync()
#To_test('abc')
