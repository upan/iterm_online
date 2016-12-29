#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#导入smtplib和MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ConfigParser
import smtplib
import sys,os

reload(sys)
sys.setdefaultencoding("utf-8")

cf = ConfigParser.ConfigParser()
cf.read("../conf/config.conf")

#mailto_list = ["liyuanchuan@variflight.com"]  #目标邮箱
#mail_host = "smtp.163.com"    
#mail_user = "liyuanchuan8@163.com"  
#mail_pass = "li6303797"  #163邮箱smtp生成的密码

mail_host = "smtp.exmail.qq.com"    
mail_user = "monitor@feeyo.com"  
mail_pass = "CTv-LIvhV%1" 


def iterm_content(iterm):
  iterm_content_file = cf.get(iterm,'ver_content')
  iterm_cont_path = '../git_download/' + iterm_content_file 
  file_object = open(iterm_cont_path)
  try:
    all_the_text = file_object.read( )
  finally:
    file_object.close( )
  return all_the_text


def send_mail(to_list, sub, content):
    me = "variflight"+"<"+mail_user+">"
    #msg = MIMEText(content,'utf-8')
    #msg = MIMEText('</pre><h1>%s</h1><pre>' % content,'html','utf-8')
    msg = MIMEText(content,'html','utf-8')
    msg['Subject'] = sub    
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

def term_subj(iterm,action):
  iterm_version = get_iterm_version(iterm)
  if action == 'test':
    sub_n = '项目' + iterm + '版本' + iterm_version + '测试上线'
  elif action == 'gray':
    sub_n = '项目' + iterm + '版本' + iterm_version +  '灰度上线'
  elif action == 'online':
    sub_n = '项目' + iterm + '版本' + iterm_version + '正式上线'
  elif action == 'test_b':
    sub_n = '项目' + iterm + '版本' + iterm_version +  '测试回退'
  elif action == 'gray_b':
    sub_n = '项目' + iterm + '版本' + iterm_version + '灰度回退'
  elif action == 'online_b':
    sub_n = '项目' + iterm + '版本' + iterm_version +  '线上回退'
  return sub_n


def term_send_content(iterm,action):
  iterm_version = get_iterm_version(iterm)
  iterm_name = cf.get(iterm,'name')
  content = iterm_content(iterm)
  git_address = cf.get(iterm,'git_address')
  if action == 'test':
    iterm_address = cf.get(iterm,'test_ip')
    iterm_name2 = iterm + '版本' + iterm_version + '测试上线'
  elif action == 'test_b':
    iterm_address = cf.get(iterm,'test_ip')
    iterm_name2 = iterm + '版本' + iterm_version +  '测试回退'
  elif action == 'gray':
    iterm_address = cf.get(iterm,'gray_ip')
    iterm_name2 = iterm + '版本' + iterm_version +  '灰度上线'
  elif action == 'gray_b':
    iterm_address = cf.get(iterm,'gray_ip')
    iterm_name2 = iterm + '版本' + iterm_version + '灰度回退'
  elif action == 'online':
    iterm_address = cf.get(iterm,'online_ip')
    iterm_name2 = iterm + '版本' + iterm_version + '正式上线'
  elif action == 'online_b':
    iterm_address = cf.get(iterm,'online_ip')
    iterm_name2 = iterm + '版本' + iterm_version +  '线上回退'
  result = '成功'
  #msg = MIMEText('</pre><h1>hello</h1><pre>','html','utf-8')
  cont = "<table align='left' border='2' cellpadding='5' cellspacing='0' width='800' style='border-collapse: collapse;'> \
　<tr>  \
　　<td> 项目名称 </td>  \
　　<td> <font color='black'> %s </font> </td>  \
　</tr>  \
　<tr>  \
　　<td> Git源码地址 </td> \
　　<td> <font color='black'> %s </font> </td>  \
　</tr>  \
　<tr>  \
　　<td> 上线地址IP </td>  \
　　<td> %s </td>  \
　</tr>  \
　<tr>  \
　　<td> 修改内容  </td>  \
　　<td> %s </td>  \
　</tr>  \
　<tr>  \
　　<td>  上线结果 </td>  \
　　<td> <font color='FF66666'> %s </font> </td>  \
　</tr>  \
  </table>  " % (iterm_name2,git_address,iterm_address,content,result)
  return cont

def get_iterm_version(iterm):
  dir_v = '../term_V_t/' + iterm
  fp_v2 = os.listdir(dir_v)
  fp_v2.sort()
  fp_ver = fp_v2[-1]
  fp_file = ''.join(fp_ver)
  return fp_file  


def term_mail(iterm,action):
  iterm_mail_address = cf.get(iterm,'mail_address')
  mail_list = eval(iterm_mail_address)
  content = term_send_content(iterm,action)
  sub = term_subj(iterm,action)
  send_mail(mail_list, sub, content)




if __name__ == '__main__':
  #iterm_content('feeyogateway')
  term_mail('feeyogateway','test')
  #fp_file = get_iterm_version('feeyogateway')

