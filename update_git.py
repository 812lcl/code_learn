#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    : update_git.py
@brief   : update code
@author  : liuchunlei <liuchunlei@baidu.com>
@date    : 2016-09-27 13:42:39
@update  : 2017-05-08 17:06:55
@version : 1.0.0.0
"""

import os
import commands


git_root = '/home/users/liuchunlei/code'

fp = open('log', 'w')
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

        cmd = "cloc %s" % dir_abspath
        fp.write(commands.getstatusoutput(cmd)[1])
        fp.write("\n")

fp.write("---- Source code learning ----\n")
fp.close()
