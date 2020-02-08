from Engine import Engine as EG
import os


ext_src = '.py'  # source extension
ext_dst = '.py'  # destination extension
namesep = '_'
Dirname = os.path.dirname(__file__)  # folder path
EGobj = EG()
EGobj.Fdir = Dirname
EGobj.ext_src = ext_src
EGobj.ext_dst = ext_dst
EGobj.namesep = namesep
EGobj.Jdir = EGobj.Fdir

# generate
EGobj.genFNJson()

# rename
# EGobj.reJsonFN()
