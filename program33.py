"""Seek() pointer in python"""

with open('file.txt','r') as f:
    print(f"Intially file pointer Position : {f.tell()}")
    print(f"Moving to postion : 12")
    f.seek(12)
    print(f"pointer Posotion now :{f.tell()}")
    print(f.read())