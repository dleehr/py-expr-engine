#!/usr/bin/env python

import json
import sys
import os # For os.path and the like

class DictWrapper(object):
    def __init__(self, d):
        self.__dict__ = d
    def eval_script(self):
        return eval(self.script) # With self as context


d = json.load(sys.stdin)
dw = DictWrapper(d)
json.dump(dw.eval_script(), sys.stdout)
