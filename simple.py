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

datfolder=os.getcwd()
filename='B2053+36_201507230240'
#readheadercmd = "readfile %s" % ('/run/media/jms03/DATA/jms_0721/'+filename+".fil")
#get timelength
#print readheadercmd
#output = getoutput(readheadercmd)
#header = {}
#for line in output.split('\n'):
#    items = line.split("=")
#    if len(items) > 1:
#        header[items[0].strip()] = items[1].strip()
#timelength=float(header["Time per file (sec)"])
#starttime=float(header["MJD start time"])
#print timelength
#print starttime
#teff=timelength

myexecute("dspsr -b 512 -nsub 200 -turns 500 -O %s %s" %(filename,'/run/media/jms03/DATA/jms_0723/'+filename+'.fil'))

#grep="grep -l '.ar' * "
#output = getoutput(grep)
#print output
#for line in output.split('\n'):
#	filename=line
#	print filename
#	if(IsSubString('.ar',filename)):
#		print "%s exist." % (filename)
#		myexecute("paz -r -E 2 -e zap %s" % (filename[:-3]+'.zap'))
#		myexecute("pav -CGTd -g%s.ps/vcps %s" % (filename[:-3]+'f_p', filename[:-3]+'.zap'))
#		myexecute("pav -CDFTd -g%s.ps/vcps %s" % (filename[:-3]+'prof', filename[:-3]+'.zap'))
#		myexecute("pav -CYFd -g%s.ps/vcps %s" % (filename[:-3]+'t_p', filename[:-3]+'.zap'))
#	else :
#		continue
#i=1
#while (i<=9999) :
#	if (i<10):
#		tem='_000'+'%d' % i
#	if (i<100 and i>=10):
#		tem='_00'+'%d' % i
#	if (i<1000 and i>=100):
#		tem='_0'+'%d' % i
#	if (i<10000 and i>=1000):
#		tem='_'+'%d' % i
#	if os.access(filename+tem+".ar",os.F_OK):
#		print "%s exist." % (filename+tem+".ar")
myexecute("paz -r -E 2 -e zap *%s" % ('.ar'))
#myexecute("pav -CGTd -g%s.ps/vcps *%s" % (filename+'f_p0', '.ar'))
#myexecute("pav -CDFTd -g%s.ps/vcps *%s" % (filename+'prof0', '.ar'))
#myexecute("pav -CYFd -g%s.ps/vcps *%s" % (filename+'t_p0', '.ar'))
myexecute("pav -CGTd -g%s.ps/vcps *%s" % (filename+'_fp', '.zap'))
myexecute("pav -CDFTd -g%s.ps/vcps *%s" % (filename+'_prof', '.zap'))
myexecute("pav -CYFd -g%s.ps/vcps *%s" % (filename+'_tp', '.zap'))
#		i=i+1
#	else:
#		break
	
	

