#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "Jialiang Zhou"
__copyright__ = "Copyright 2019, The *** Project"
__version__ = "1.0.0"
__email__ = "zhoujlsem@gmail.com"
__phone__ = "15990161157"
__description__ = "检索项目关键字信息"
__usage__ = "python keywords.py file_path -k keyword_1 keyword_2 ..."

import os
import argparse


# 单文件查询关键字信息
def check_one_file(file_path, keywords):
    print('File path: {}'.format(file_path))
    with open(file_path, 'r') as f:
        idx_line = 1
        for line in f:
            for keyword in keywords:
                if keyword in line:
                    print('\tline: {}; keyword: {}'.format(idx_line, keyword))
            idx_line += 1


if __name__ == '__main__':

    # 参数
    parser = argparse.ArgumentParser('Check keywords in project'
                                     'Usage: python keywords.py file_path -k keyword_1 keyword_2 ...')
    parser.add_argument('project_path')
    parser.add_argument('-k', '--keywords', nargs='+')
    args = parser.parse_args()
    project_path = args.project_path
    keywords = args.keywords


    # 遍历项目文件
    for filename in os.listdir(project_path):
        if filename[0] != '.':
            file_path = os.path.join(project_path, filename)
            check_one_file(file_path, keywords)


