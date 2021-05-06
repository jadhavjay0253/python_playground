# WAP TO RENAME A FILE AS RENAMED_BY_PYTHON.TXT
import os

old_name = "os.txt"
new_name = "renamed_by_python.txt"

with open(old_name) as f:
    dt1 = f.read()

with open(new_name,'w') as f:
    f.write(dt1)

os.remove(old_name)
print("File renamed sucessfully!")