from fabric.api import *
import time

env.user = 'bender'
env.shell = '/bin/bash -c'

# Checkout updated code
def deploy(giturl, gitrepo, gitbranch, deploydir):
  print "===> Pulling updated code from git repository"
  with prefix("cd %s" %(deploydir)):
    run("git pull --rebase --verbose")
    run("git checkout %s" %(gitbranch))
