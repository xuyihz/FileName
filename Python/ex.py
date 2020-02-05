from Engine import Engine as EG
import os


ext_src = '.py'  # source extension
ext_dst = '.py'  # destination extension
namesep = '_'
Dirname = os.path.dirname(__file__)  # folder path
EGobj = EG(Dirname, ext_src, ext_dst, namesep)

# generate
EGobj.genFNJson()

# rename
# EGobj.reJsonFN()
