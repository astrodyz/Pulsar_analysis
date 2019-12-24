#!/usr/bin/python
#from numpyio import fread, fwrite
import os
from sys import argv
from commands import getoutput

def myexecute(cmd):
    print "********************************"
    print "%s"%cmd
    print "--------------------------------"
    os.system(cmd)

def IsSubString(SubStrList,Str): 
 flag=False
 for substr in SubStrList: 
  if not(substr in Str): 
   flag=True
 return flag 

def process(name)
    datname=name
    datfolder=os.getcwd()
    toolfolder="/home/jms03/PSR_Tool_zmtt/Raw2FITS"
    prodatafolder="/run/media/jms03/DATA/jms0615_S/"
    Tfold=20.0
    nbin=512
    #--------------------------- Raw to psrfits 
    if os.access(datname+".dat.right",os.F_OK):
        print "%s exist." % (datname+".dat.right")
    else:
        os.chdir(toolfolder)
        myexecute("./readRawDataHead %s" % (datfolder+"/"+datname+".dat"))
        myexecute("emacs Raw2FITS_V2.c &")
        myexecute("./makeR2F Raw2FITS_V2")
        myexecute("./Raw2FITS_V2 %s" % (datfolder+"/"+datname+".dat"))
        os.chdir(datfolder)

    #--------------------------- psrfits to filterbank 
    if os.access(datname+".fil",os.F_OK):
        print "%s exist." % (datname+".fil")
    else:
        myexecute("filterbank %s > %s" % (datname+".dat.right",prodatafolder+datname+".fil"))
    #   myexecute("filterbank %s > %s" % (datname+".dat.right",datname+".fil"))
    os.chdir(prodatafolder)



#print "\nProcessing file: %s" % argv[1]
#datname=argv[1][:-4]
#datname="psrJ1022+1001_201506251740"
#datfolder=os.getcwd()
#toolfolder="/home/jms03/PSR_Tool_zmtt/Raw2FITS"
#prodatafolder="/run/media/jms03/DATA/jms0615_S/"
#Tfold=20.0
#nbin=512


readfilename = 'ls *.dat'
namelist = getoutput(readfilename)
for line in namelist.split('\n'):
    datname = line
    if IsSubString('3C',datname)
        print datname
        process(datname)
	

