#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()

parser.add_option('-u','--user',dest='user',action='store',type=str,metavar='user',help='Enter User Name!!')
parser.add_option('-p','--port',dest='port',type=int,metavar='user',help='Enter Mysql Port!!')
parser.add_option('-v',help='Mysql Version!!')

parser.set_defaults(v=1.2)
options,args=parser.parse_args()
print 'OPTIONS:' ,options
print 'ARGS:',args

print '~'*20
print 'user:' ,options.user
print 'port:' ,options.port
print 'version:',options.v
