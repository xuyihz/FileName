# JsonFile class
# Xu Yi
# 2020

import os
import json


class JsonFile(object):

    def __init__(self, Jdir, Jname, Jencode):
        self.Jdir = Jdir
        self.Jname = Jname
        self.Jext = '.json'
        self.Jpath = os.path.join(Jdir, (Jname+self.Jext))
        self.Jencode = Jencode

    def readJson(self):
        with open(self.Jpath, 'r+', encoding=self.Jencode) as f:
            data = json.load(f)
            return data
    
    def writeJson(self, data, Jindent, Jsort):
        with open(self.Jpath, 'a+', encoding=self.Jencode) as f:
            # 'a': open for writing, appending to the end of the file if it exists
            # '+': open for updating (reading and writing)
            json.dump(data, f, ensure_ascii=False, indent=Jindent, sort_keys=Jsort)
