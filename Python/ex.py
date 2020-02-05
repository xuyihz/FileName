from Engine import Engine as EG
import os


ext_src = '.py'  # source extension
ext_dst = '.py'  # destination extension
namesep = '_'
Dirname = os.path.dirname(__file__)  # folder path
EGobj = EG(Dirname)

# generate
EGobj.genFNJson(ext_src, namesep)

# rename
# EGobj.reJsonFN(ext_src, ext_dst, namesep)
