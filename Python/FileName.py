# FileName class
# Xu Yi
# 2020

import os


class FileName(object):

    def __init__(self, path):
        self.path = path
        self.DirName = os.path.dirname(path)
        basename = os.path.basename(path)
        (self.Name, self.Extension) = os.path.splitext(basename)
