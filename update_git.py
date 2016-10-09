#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    : update_git.py
@brief   : update code
@author  : liuchunlei <liuchunlei@baidu.com>
@date    : 2016-09-27 13:42:39
@update  : 2016-10-09 21:03:09
@version : 1.0.0.0
"""

import os
import commands


git_root = '/home/users/liuchunlei/code'

with open('code_list', 'r') as f:
    print "---- Source code learning ----"
    print
    for line in f:
        remote_path = line.split('#')[0].strip('\t\n\r')
        if remote_path == '':
            continue
        if remote_path.startswith('https://github.com') is False:
            continue

        dir_name = os.path.basename(remote_path).split('.')[0]
        dir_abspath = os.path.abspath(dir_name)
        print dir_abspath
        if os.path.exists(dir_abspath):
            cmd = 'cd %s && git pull && cd - > /dev/null' % dir_abspath
            ret = commands.getstatusoutput(cmd)
            if ret[0] == 0:
                print ret[1]
            else:
                print 'failed, retry...'
                ret = commands.getstatusoutput(cmd)
                print ret[1]
        else:
            cmd = 'git clone %s' % remote_path
            ret = commands.getstatusoutput(cmd)
            if ret[0] == 0:
                print ret[1]
            else:
                print 'failed, retry...'
                ret = commands.getstatusoutput(cmd)
                print ret[1]

        cmd1 = "find %s -name \"*.py\" | wc -l" % dir_abspath
        print "Python files: %s" % commands.getstatusoutput(cmd1)[1]
        cmd2 = "find %s -name \"*.py\" | xargs wc -l | tail -1 | awk '{print $1}'" % dir_abspath
        print "Python lines: %s" % commands.getstatusoutput(cmd2)[1]
        cmd3 = "find %s -name \"*.c\" -o -name \"*.cpp\" -o -name \"*.h\" | wc -l" % dir_abspath
        print "C files: %s" % commands.getstatusoutput(cmd3)[1]
        cmd4 = "find %s -name \"*.c\" -o -name \"*.cpp\" -o -name \"*.h\" | xargs wc -l | tail -1 | awk '{print $1}'" % dir_abspath
        print "C lines: %s" % commands.getstatusoutput(cmd4)[1]
        cmd5 = "find %s -name \"*.c\" -o -name \"*.sh\"| wc -l" % dir_abspath
        print "Shell files: %s" % commands.getstatusoutput(cmd5)[1]
        cmd6 = "find %s -name \"*.c\" -o -name \"*.sh\"| xargs wc -l | tail -1 | awk '{print $1}'" % dir_abspath
        print "Shell lines: %s" % commands.getstatusoutput(cmd6)[1]
        print

print "---- Source code learning ----"
