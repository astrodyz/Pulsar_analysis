#!/usr/bin/python
import os
from sys import argv
from commands import getoutput

def IsSubString(SubStrList,Str): 
 flag=True
 for substr in SubStrList: 
  if not(substr in Str): 
   flag=False
 return flag 


def myexecute(cmd):
    print "********************************"
    print "%s"%cmd
    print "--------------------------------"
    os.system(cmd)

filename='B2053+36_201507230240'
myexecute("pav -CGTd -g%s.ps/vcps *%s" % (filename+'_fp', '.zap'))
myexecute("pav -CDFTd -g%s.ps/vcps *%s" % (filename+'_prof', '.zap'))
myexecute("pav -CYFd -g%s.ps/vcps *%s" % (filename+'_tp', '.zap'))
myexecute("pav -CGTd -z 0.4,0.6 -g%s.ps/vcps *%s" % (filename+'_fp_zoom', '.zap'))
myexecute("pav -CDFTd -z 0.4,0.6 -g%s.ps/vcps *%s" % (filename+'_prof_zoom', '.zap'))
myexecute("pav -CYFd -z 0.4,0.6 -g%s.ps/vcps *%s" % (filename+'_tp_zoom', '.zap'))

#		i=i+1
#	else:
#		break
	
	

