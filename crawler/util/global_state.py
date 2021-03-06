#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'CwT'

# store all global variables in this file
ALL = {
    "CURRENT_DEPTH": 0,
    "SERVER_IP": "127.0.0.1",
    "SERVER_PORT": 8775
}

class State(object):
    def __init__(self):
        self.__dict__.update(ALL)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__[item]

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

