# mine a log file and search if it contains 'python or not'

with open("D:/Work/Python/Learning/Files I/O/log.txt") as f:
    data = f.read().lower() # to search while keeping all data lowered

if "python" in data:
    print("Yes it contains 'python'.")
else:
    print("No it doesn't contains 'python'.")