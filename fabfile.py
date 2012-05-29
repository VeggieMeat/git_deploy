from fabric.api import *
from fabric.contrib.files import exists
import time

env.user = 'bender'
env.shell = '/bin/bash -c'

# Checkout updated code
def deploy(giturl, gitrepo, gitbranch, deploydir):
  print "===> Checking that deployment directory exists"
  if not exists(deploydir, use_sudo=False, verbose=True):
    print "===> Cloning git repository"
    run("git clone %s:%s %s" %(giturl, gitrepo, deploydir))
  print "===> Pulling updated code from git repository"
  with prefix("cd %s" %(deploydir)):
    run("git pull --rebase --verbose")
    run("git checkout %s" %(gitbranch))