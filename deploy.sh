#!/bin/bash
#
# Wrapper script for our fabfile to be called from Jenkins
#

# Where our fabfile is
FABFILE=/usr/local/bin/git_deploy/fabfile.py

HOST=$1
GITURL=$2
GITREPO=$3
GITBRANCH=$4
DEPLOYDIR=$5

if [[ -z $HOST ]] || [[ -z $GITURL ]] || [[ -z $GITREPO ]] || [[ -z $GITBRANCH ]] || [[ -z $DEPLOYDIR ]]
then
  echo "Missing arguments! Exiting"
  exit 1
fi

fab -f $FABFILE -H $HOST deploy:giturl=$GITURL,gitrepo=$GITREPO,gitbranch=$GITBRANCH,deploydir=$DEPLOYDIR || exit 1
