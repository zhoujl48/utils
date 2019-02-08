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


# 是否文本
def is_text(file_path):
    if os.path.isdir(file_path):
        print('Is directory: {}'.format(file_path))
        return False
    elif file_path[-4:] == '.pyc':
        print('Not a text file: {}'.format(file_path))
        return False
    else:
        return True


# 单文件查询关键字信息
def check_one_file(file_path, keywords):
    print('File path: {}'.format(file_path))
    with open(file_path, 'r', encoding='utf-8') as f:
        idx_line = 1
        for line in f:
            for keyword in keywords:
                if keyword in line:
                    print('\tline {}, keyword: {}'.format(idx_line, keyword))
            idx_line += 1


if __name__ == '__main__':

    # 参数
    parser = argparse.ArgumentParser('Check keywords in project'
                                     'Usage: python keywords.py file_path -k keyword_1 keyword_2 ...')
    parser.add_argument('project_path', help='Source of project where keywords need checking')
    parser.add_argument('-k', '--keywords', nargs='+', help='List of keywords')
    args = parser.parse_args()
    project_path = args.project_path
    keywords = args.keywords


    # 遍历项目文件
    for filename in os.listdir(project_path):
        file_path = os.path.join(project_path, filename)
        if is_text(file_path):
            check_one_file(file_path, keywords)


