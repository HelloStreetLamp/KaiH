#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = loggings.py
__author__ = whyk
__create_time__ = 2021/10/24
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import os
import argparse
from typing import Optional


_default_handler: Optional[logging.Handler] = None

log_levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}


def get_logger(args):
    log_path = os.path.join(args.root_path, 'logs', args.mode, '{}.log'.format(args.id))
    print(log_path)


def test():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default='default', help='action id')
    parser.add_argument('--mode', choices=['train', 'test', 'evaluate'], default='train', help='choose a mode')
    parser.add_argument('--root-path', metavar='path', type=str, default='/home/whyk/project/fantastic_dl_structure',
                        help='root path')
    args = parser.parse_args()
    get_logger(args)


if __name__ == '__main__':
    test()

