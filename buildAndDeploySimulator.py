import sys
from optparse import OptionParser
import os
from os import chdir
import subprocess
import shlex
codes = {'FAILED':1,'SUCCESS':0}

def parse_options():
    try:
        parser = OptionParser()
        parser.add_option("-u", "--repo_url", action="store",
                          default="", dest="repo_url",
                          help="The branch used for this coverage Information")
        parser.add_option("-b", "--branch", action="store",
                          default="master", dest="branch_no",
                          help="The branch used for this coverage Information")
        (options,args) = parser.parse_args()
        return {"repo_url":options.repo_url,"branch":options.branch_no}
    except Exception, e:
        print "\nException Occurred %s. Please Check" %(e)
        return codes['FAILED']

def parseBoolOpts(value):
     value = True
     if (str(value).lower()=="false" or value is None):
         value=False
     return value
    

def init():
    try:
        options_dict = parse_options()
        return options_dict
    except Exception, e:
        print "\nException Occurred under init. Please Check:%s" %(e)
        sys.exit(1)


def execCmd(cmd):
    pipe = subprocess.PIPE
    print shlex.split(cmd)
    proc = subprocess.check_call(shlex.split(cmd))
    print proc
    print dir(proc)
    return proc 


def buildSimulator(retryBuild):
    try:
        out=None
        print "================== Building Simulator Started ================"
        while (out!=0 and retryBuild!=0):
            try:
              os.chdir("/automation/cloudstack")
              os.system ("sudo killall -9 java")
              out=execCmd("sudo mvn clean install -P developer -Dsimulator -DskipTests")
            except Exception, e:
              print ("sudo mvn clean  install failed, will retry")
              print e
            retryBuild=retryBuild-1
        if out != 0:
            sys.exit(1)

        os.system("sudo mvn -Pdeveloper -pl developer -Ddeploydb")
        os.system("sudo mvn -Pdeveloper -pl developer -Ddeploydb-simulator")
        os.system("sudo mysql -uroot  -e GRANT ALL PRIVILEGES ON *.* TO \'root\'@\'localhost\' WITH GRANT OPTION")
        print "==== Starting Simulator ===="
        os.system("sudo mvn -Dsimulator -pl client jetty:run &")
        print "==== Simulator Successfully Started ===="
    except Exception, e:
        print "==== Building Simulator Failed ===="
        print e
        sys.exit(1)


def getCSCode(inp_dict):
    repo_url = inp_dict['repo_url']
    branch = inp_dict['branch']
    os.system("sudo rm -rf /automation")
    os.system("sudo mkdir -p /automation")
    os.chdir("/automation/")
    os.system("sudo git init;git clone %s "%repo_url)
    os.system("sudo git fetch origin %s"%branch)
    os.system("sudo git reset --hard")
    os.system("sudo git checkout -b %s FETCH_HEAD"%(branch))

def runDeployDc():
    print "==== Deploy DataCenter Started ===="  
    os.system("sudo python2.7 /automation/cloudstack/tools/marvin/setup.py install")
    os.system("sudo python2.7 /automation/cloudstack/tools/marvin/marvin/deployDataCenter.py -i /automation/cloudstack/setup/dev/advanced.cfg")
    print "==== Deploy DataCenter Successfull===="  

def main():
     ret = init()
     '''
     Step1: Get CS Code and bring Simulator Up  
     ''' 
     getCSCode(ret)
     '''
     Step2 :Build Simulator
     ''' 
     buildSimulator(3)  
     '''
     Step3: Run Deploy DC  
     ''' 
     runDeployDc()

if __name__ == '__main__':
     main()        
