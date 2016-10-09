#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    : update_git.py
@brief   : update code
@author  : liuchunlei <liuchunlei@baidu.com>
@date    : 2016-09-27 13:42:39
@update  : 2016-10-09 21:35:30
@version : 1.0.0.0
"""

import os
import commands


git_root = '/home/users/liuchunlei/code'

fp = open('log', 'a')
with open('code_list', 'r') as f:
    fp.write("---- Source code learning ----\n")
    fp.write("\n")
    for line in f:
        remote_path = line.split('#')[0].strip('\t\n\r')
        if remote_path == '':
            continue
        if remote_path.startswith('https://github.com') is False:
            continue

        dir_name = os.path.basename(remote_path).split('.')[0]
        fp.write(dir_name+"\n")
        dir_abspath = os.path.abspath(dir_name)
        if os.path.exists(dir_abspath):
            cmd = 'cd %s && git pull && cd - > /dev/null' % dir_abspath
            ret = commands.getstatusoutput(cmd)
            if ret[0] == 0:
                fp.write(ret[1]+"\n")
            else:
                fp.write('failed, retry...\n')
                ret = commands.getstatusoutput(cmd)
                fp.write(ret[1]+"\n")
        else:
            cmd = 'git clone %s' % remote_path
            ret = commands.getstatusoutput(cmd)
            if ret[0] == 0:
                fp.write(ret[1]+"\n")
            else:
                fp.write('failed, retry...\n')
                ret = commands.getstatusoutput(cmd)
                fp.write(ret[1]+"\n")

        cmd1 = "find %s -name \"*.py\" | wc -l" % dir_abspath
        fp.write("Python files: %s" % commands.getstatusoutput(cmd1)[1]+"\n")
        cmd2 = "find %s -name \"*.py\" | xargs wc -l | tail -1 | awk '{print $1}'" % dir_abspath
        fp.write("Python lines: %s" % commands.getstatusoutput(cmd2)[1]+"\n")
        cmd3 = "find %s -name \"*.c\" -o -name \"*.cpp\" -o -name \"*.h\" | wc -l" % dir_abspath
        fp.write("C files: %s" % commands.getstatusoutput(cmd3)[1]+"\n")
        cmd4 = "find %s -name \"*.c\" -o -name \"*.cpp\" -o -name \"*.h\" | xargs wc -l | tail -1 | awk '{print $1}'" % dir_abspath
        fp.write("C lines: %s" % commands.getstatusoutput(cmd4)[1]+"\n")
        cmd5 = "find %s -name \"*.c\" -o -name \"*.sh\"| wc -l" % dir_abspath
        fp.write("Shell files: %s" % commands.getstatusoutput(cmd5)[1]+"\n")
        cmd6 = "find %s -name \"*.c\" -o -name \"*.sh\"| xargs wc -l | tail -1 | awk '{print $1}'" % dir_abspath
        fp.write("Shell lines: %s" % commands.getstatusoutput(cmd6)[1]+"\n")
        fp.write("\n")

fp.write("---- Source code learning ----\n")
fp.close()
