#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sergey_Matusevich"

FILE_IN = 'D:\SHTests-master\SHTests-master\src\lorem_ipsum.2txt.txt'
FILE_OUT = r'D:\SHTests-master\SHTests-master\src\truncated_lorem_ipsum.txt'


def ipsum():
    try:
        with open(FILE_IN,
                  'r') as file:
            with open(FILE_OUT, 'w') as file2:
                for _, i in zip(range(10), file):
                    file2.write(i)
    except FileNotFoundError:
        print('File Not Found Error')


ipsum()
