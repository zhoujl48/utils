#!/usr/bin/python
# -*- coding:utf-8 -*-
#!/usr/bin/python
# -*- coding:utf-8 -*-
################################################################################
#
# Copyright (c) 2019 ***.com, Inc. All Rights Reserved
# The Common Tools Project
################################################################################
"""
常用工具类 -- 关键字符串查询

Usage: python keywords.py file_path -k keyword_1 keyword_2 ...
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019/02/13
"""
import io
import sys
import os
import argparse
import logging
import log


# Unix系统打印中文
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


# 是否文本
def is_text(file_path):
    if os.path.isdir(file_path):
        logging.info('Is directory: {}'.format(file_path))
        return False
    elif file_path[-4:] == '.pyc':
        logging.info('Not a text file: {}'.format(file_path))
        return False
    else:
        return True


# 单文件查询关键字信息
def check_one_file(file_path, keywords):
    logging.info('Start checking file path: {}'.format(file_path))
    with open(file_path, 'r', encoding='utf-8') as f:
        idx_line = 1
        for line in f:
            for keyword in keywords:
                if keyword in line:
                    logging.info('Line {}, Keyword: {}, Content: {}'.format(idx_line, keyword, line.strip()))
            idx_line += 1


if __name__ == '__main__':

    # 参数
    parser = argparse.ArgumentParser('Check keywords in project'
                                     'Usage: python keywords.py file_path -k keyword_1 keyword_2 ...')
    parser.add_argument('project_path', help='Source of project where keywords need checking')
    parser.add_argument('-k', '--keywords', nargs='+', help='List of keywords')     # nargs='+'能够将多个参数组合成一个list
    args = parser.parse_args()
    project_path = args.project_path
    keywords = args.keywords
    
    # Init Log
    log.init_log('./logs/keywords')


    if os.path.isdir(project_path):
        # 遍历项目文件
        for filename in os.listdir(project_path):
            file_path = os.path.join(project_path, filename)
            if is_text(file_path):
                check_one_file(file_path, keywords)
    else:
        file_path = project_path
        if is_text(file_path):
            check_one_file(file_path, keywords)
        else:
            logging.warning('Not a text file: {}'.format(file_path))


