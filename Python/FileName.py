# FileName class
# Xu Yi
# 2020

import os


class FileName(object):

    def __init__(self, path, namesep):
        self.path = path
        self.DirName = os.path.dirname(path)
        self.basename = os.path.basename(path)
        (self.Name, self.Extension) = os.path.splitext(self.basename)
        self.NameSplit = self.Name.split(namesep)
