#!/usr/bin/env python

import os
import this

class Phone(object):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def resolution(self):
        return self.width * self.height
