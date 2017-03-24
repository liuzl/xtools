#!/bin/sh

CWD=`cd $(dirname $0); pwd`

chmod u+x $CWD/xgo
chmod u+x $CWD/xcp
chmod u+x $CWD/xmon
chmod u+x $CWD/xrun
chmod 600 $CWD/xtools.ini

[ -f ~/.profile ] && echo "PATH=\$PATH:$CWD" >> ~/.profile
[ -f ~/.bashrc ] && echo "PATH=\$PATH:$CWD" >> ~/.bashrc
[ -f ~/.bash_profile ] && echo "PATH=\$PATH:$CWD" >> ~/.bash_profile

echo 'reconnect the shell or input source ~/.bashrc'
