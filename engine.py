#!/usr/bin/env python

import json
import sys
import os   # For os.path and the like


class DictWrapper(object):
    def __init__(self, d):
        self.__dict__ = d

    def eval_script(self):
        return eval(self.script)  # With self as context

    def __getattr__(self, attr):
        return None


if __name__ == '__main__':
    input_dict = json.load(sys.stdin)
    dw = DictWrapper(input_dict)
    json.dump(dw.eval_script(), sys.stdout)
