#!/usr/bin/env python

import commands
import global_setting
from up_logs import new_logs
import sys

logs = new_logs.Loggger()


def SaltApi(ip,cmd):
  sal_cmd = 'salt %s cmd.run "%s"' % (ip,cmd)
  (status,result) = commands.getstatusoutput(sal_cmd)
  if status == 0:
    logs.info_all('%s excute "%s" success ' %(ip,cmd))
  else:
    logs.error_all('%s excute "%s" false ' %(ip,cmd) )
    print result
    sys.exit()



#SaltApi('192.168.2.202','rsync -vzrtopg --progress --delete root@192.168.2.204::test /tmp/ --password-file=/etc/rsync.secret')
