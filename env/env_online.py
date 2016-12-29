#!/usr/bin/env python
#coding:utf-8 

import global_setting
from up_logs import new_logs
import string,os,sys
import ConfigParser
import re
import commands


path = os.getcwd()
parent_path = os.path.dirname(path)

logs = new_logs.Loggger()


#找文件所在下载的git包中的路径
def search(path,word):
  ##查找文件所在的文件路径
  file_cmd = 'find ' + ' ' + parent_path + '/'  + 'git_download' + '/' + path  + ' ' + '-name' + ' ' + word
  Find_r = commands.getoutput(file_cmd)
  return Find_r

##换线上包中的配置文件
def online_replace(self):
  ##获取项目的配置文件
  cf = ConfigParser.ConfigParser()
  cf.read("../conf/config.conf")
  ##获取项目配置文件中需要替换的文件
  option = cf.options(self)
  local_n = [elem for elem in option if 'local' in elem]
  ##把/replace_file/文件下需要替换的文件替换到项目中
  for i in local_n:
    iterm_file = cf.get(self,i)
    iterm_name = os.path.basename(iterm_file)
    file_path = search(self,iterm_name)
    if file_path == '':
      logs.error_all('%s config %s is Not exits' %(self,i))
      sys.exit()
    else:
      cp_cmd = 'cp -rf ' + parent_path + '/replace_file_on/' + self + '/' + iterm_name + ' '  + file_path
      ##执行替换命令
      (Re,Out) = commands.getstatusoutput(cp_cmd)
      if Re == 0:
        logs.info_all('replace %s success' % file_path)
      else:
        print Out
        logs.error_all('replace %s False!!!'  % file_path)
        sys.exit()
    

##创建测试项目版本文件夹
def create_version_file(self):
  ##创建项目版本文件夹
  Get_term_path = parent_path + '/term_V_on/' 
  fp = os.listdir('../term_V_on')
  if self not in fp:
    mk_cmd = 'mkdir ' + Get_term_path + self
    os.system(mk_cmd)
    logs.info_all('mkdir %s%s success' %(Get_term_path,self))
    mk_cmd_v = 'mkdir ' + Get_term_path + self + '/' + 'v1.0'
    os.system(mk_cmd_v)
    logs.info_all('mkdir %s%s/v1.0 success' %(Get_term_path,self))
  else:
    fp_file = get_new_version(self)
    v_cmd = "echo %s | awk -Fv  '{print $2}' " % fp_file
    v_result = commands.getoutput(v_cmd)
    v_result = float(v_result)
    v_result += 0.1
    mk_cmd_v2 = 'mkdir ' + Get_term_path + self + '/' + 'v' + str(v_result)
    os.system(mk_cmd_v2)
    logs.info_all('success mkdir %s%s/v%s' % (Get_term_path,self,v_result))
  

##生成项目版本
def file_create_version(iterm):
  ##生成项目版本号
  fp_file = get_new_version(iterm)
  file_r = 'cp -r ' +  parent_path  + '/git_download/' + iterm + ' '  + parent_path + '/term_V_on/' +  iterm + '/' + fp_file + '/'
  (Re,Out) = commands.getstatusoutput(file_r)
  if Re == 0:
    logs.info_all('cp %s to %s success' %(iterm,file_r))
  else:
    print Out
    logs.error_all('something happen error')
 

##生成在/term_V_on/下的最新包 
def file_create_online(iterm):
  online_replace(iterm)
  create_version_file(iterm)
  file_create_version(iterm)
  ##删除原有的项目包
  iterm_r_cmd = 'rm -rf ' + parent_path + '/Iterm/' + '/term_V_on/' + iterm 
  (Re,Out) = commands.getstatusoutput(iterm_r_cmd)
  if Re == 0:
    logs.info_all('rm %s/term_V_on/%s success' %(parent_path,iterm))
  else:
    logs.error_all('rm %s/iterm_on/%s false' %(parent_path,iterm))
    sys.exit()
  fp_file = get_new_version(iterm)
  ##最新版本的包复制到/Iterm/term_V_on/下
  file_r = 'cp -r ' + parent_path + '/term_V_on/' +  iterm + '/' + fp_file + '/' +  iterm  + ' ' + parent_path + '/Iterm/iterm_on/'
  (Re,Out) = commands.getstatusoutput(file_r)
  if Re == 0:
    logs.info_all('cp new_version to %s/Iterm/term_on/%s' %(parent_path,iterm))
  else:
    logs.error_all('action: %s false' % file_r)
    print Out
    sys.exit()


##回退测试的上一个版本的内容在/Iterm/iterm_on下
def Rollback(iterm):
  ite_on_cmd = 'rm -rf ' + parent_path + '/Iterm/iterm_on/' + iterm
  (Re,Out) = commands.getstatusoutput(ite_on_cmd)
  if Re == 0:
    logs.info('rm %s/Iterm/iterm_on/%s success' %(parent_path,iterm))
  else:
    logs.error_all('something error happend')
  ter_v = get_new_version(iterm)
  ite_r_ver = 'rm -rf ' + parent_path + '/term_V_on/' +  iterm + '/'  + ter_v
  (Re,Out) = commands.getstatusoutput(ite_r_ver)
  ter_v = get_new_version(iterm)
  ter_c = 'cp -r ' + parent_path + '/term_V_on/' +  iterm + '/' + ter_v + '/' +  iterm  + ' ' + parent_path + '/Iterm/iterm_on/'
  (Re,Out) = commands.getstatusoutput(ter_c)
  if Re == 0:
    logs.info_all('Now already back to %s in %s/Iterm/iterm_on/%s' %(ter_v,parent_path,iterm))


##获取最新版本名
def get_new_version(iterm):
  dir_v = parent_path + '/term_V_on/' + iterm
  fp_v2 = os.listdir(dir_v)
  fp_v2.sort()
  try:
    fp_ver = fp_v2[-1]
    fp_file = ''.join(fp_ver)
    return fp_file
  except IndexError:
    fp_file = "v1.0"
    return fp_file


#file_create_online('abc')
#get_new_version('abc')

#search('abc','test')
#online_test('abc')
#term_version('abc')

#file_move('abc')

#online_test('abc')
#create_version_file('abc')
#file_create_version('abc')
#file_create_online('abc')

#Rollback('abc')
