from Engine import Engine as EG
import os


ext = '.txt'
namesep = '_'
Dirname = os.path.dirname(__file__)
EGobj = EG(Dirname)

# generate
EGobj.genFNJson(ext, namesep)

# rename
EGobj.reJsonFN(ext, namesep)
