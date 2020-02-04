import FileName as FN

path = "C:/Users/XYGC/Desktop/FileName/Python/ex.py"
a = FN.FileName(path)

print("path = ", a.path)
print("DirName = ", a.DirName)
print("Name = ", a.Name)
print("Extension = ", a.Extension)
