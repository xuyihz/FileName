import FileName as FN
import json
import os

Dirname = os.path.dirname(__file__)
basename = "ex_1.py"
# Join one or more path components intelligently. '\\'
path = os.path.join(Dirname, basename)
namesep = '_'
a = FN.FileName(path, namesep)

print("path = ", a.path)
print("DirName = ", a.DirName)
print("Name = ", a.Name)
print("NameSplit = ", a.NameSplit)
print("Extension = ", a.Extension)

print(a.__dict__)
print(json.dumps(a.__dict__))

data_list = a.__dict__

# with open('data2.json', 'w+', encoding='utf-8') as f:
#     # 'w': open for writing, truncating the file first
#     # '+': open for updating (reading and writing)
#     json.dump(data_list, f, ensure_ascii=False, indent=4, sort_keys=True)


# with open('data2.json', 'r+', encoding='utf-8') as f:
#     data = json.load(f)

# print('data = ', data)

# try:
#     # On Windows, if dst exists a FileExistsError is always raised.
#     os.rename('data2.json', 'data0.json')
# except expression as identifier:  # need to be modified
#     pass


with os.scandir(Dirname) as DEit:
    for entry in DEit:
        (dirname, extension) = os.path.splitext(entry.path)
        if extension == ".py":
            print(entry.name)

# with os.scandir(data_path) as it:
#     for entry in it:
#         if not entry.name.startswith('.') and entry.is_file():
#             file_name=entry.name
#             pair='__'.join(file_name.split('__')[:2])
#             shutil.move(data_path+file_name,target_path+pair+'/'+file_name)
#             print(file_name)

# for i in SubDir:
#     path = os.path.join(dir, i)
#     if os.path.isdir(path):
#         end_dir = os.listdir(path)
#         for i in range(len(end_dir)):
#             newname = end_dir[i][0:50]
#             os.rename(os.path.join(path, end_dir[
#                       i]), os.path.join(path, newname))
